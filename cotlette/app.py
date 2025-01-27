import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route

from jinja2 import FileSystemLoader, Environment


class Cotlette(Starlette):
    def __init__(self, templates_dir="templates", *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Текущая директория фреймворка
        framework_dir = os.path.dirname(os.path.abspath(__file__))

        # Путь к директории шаблонов внутри фреймворка
        framework_templates_dir = os.path.join(framework_dir, "templates")

        # Подключам шаблоны
        # self.templates = Jinja2Templates(directory=templates_dir)
        self.templates = Jinja2Templates(directory=framework_templates_dir)

        # Дополнительные директории для шаблонов (например, пользовательские)
        custom_templates_dir = os.path.abspath("templates")
        override_templates_dir = os.path.abspath("override/templates")

       # Создаем Jinja2 Environment с загрузчиком для нескольких директорий
        self.jinja_env = Environment(loader=FileSystemLoader([
            override_templates_dir,
            framework_templates_dir,
            custom_templates_dir
        ]))

        # Передаем настроенное окружение Jinja2 в Starlette Templates
        self.templates = Jinja2Templates(env=self.jinja_env)
        
        self._initialize_internal_routes()
        self.spec = APISpec(
            title="Cotlette API",
            version="1.0.0",
            openapi_version="3.0.3",
            plugins=[MarshmallowPlugin()],
        )
    
    def _initialize_internal_routes(self):
        """Инициализация внутренних маршрутов фреймворка"""
        self.router.routes.append(Route("/admin", self.admin_home, methods=["GET"]))
        self.router.routes.append(Route("/docs", self.swagger_ui, methods=["GET"]))
        self.router.routes.append(Route("/openapi.json", self.openapi_json, methods=["GET"]))
    
    async def swagger_ui(self, request):
        """Swagger UI"""
        swagger_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Swagger UI</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui.css">
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui-bundle.js"></script>
            <script>
                const ui = SwaggerUIBundle({
                    url: '/openapi.json',
                    dom_id: '#swagger-ui',
                });
            </script>
        </body>
        </html>
        """
        return HTMLResponse(swagger_template)
    

    async def openapi_json(self, request):
        """Возвращает OpenAPI-спецификацию"""
        return JSONResponse(self.spec.to_dict())


    def add_route(self, path, endpoint=None, methods=["GET"], summary=None, description=None):
        """Метод, чтобы использовать как декоратор"""
        def decorator(func):
            # Добавление маршрута
            self.router.routes.append(Route(path, func, methods=methods))

            # Добавляем маршрут в OpenAPI
            operations = {}
            for method in methods:
                operations[method.lower()] = {
                    "summary": summary or "No summary",
                    "description": description or "No description",
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                        }
                    },
                }
            self.spec.path(path=path, operations=operations)
            return func

        # Если endpoint передан, сразу добавляем маршрут
        if endpoint:
            return decorator(endpoint)
        return decorator
    
    async def admin_home(self, request):
        """Обработчик для /admin"""
        # return HTMLResponse("<h1>Admin Dashboard</h1>")
        return await self.render_template(request, "dashboard.html", context={})

    async def render_template(self, request, template_name, context):
        context["request"] = request
        return self.templates.TemplateResponse(template_name, context)

    async def json(self, data, status_code=200):
        return JSONResponse(content=data, status_code=status_code)
    
    async def __call__(self, scope, receive, send):
        """Основной метод обработки запросов"""
        if scope["type"] == "http":
            await self.router(scope, receive, send)
        else:
            raise NotImplementedError("Тип запроса не поддерживается")
