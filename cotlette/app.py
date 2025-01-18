# cotlette/app.py
from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route

class Cotlette(Starlette):
    def __init__(self, templates_dir="templates", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.templates = Jinja2Templates(directory=templates_dir)
        self._initialize_internal_routes()
    
    def _initialize_internal_routes(self):
        """Инициализация внутренних маршрутов фреймворка"""
        self.router.routes.append(Route("/admin", self.admin_home, methods=["GET"]))
    
    async def admin_home(self, request):
        """Обработчик для /admin"""
        return HTMLResponse("<h1>Admin Dashboard</h1>")

    async def render_template(self, request, template_name, context):
        context["request"] = request
        return self.templates.TemplateResponse(template_name, context)

    async def json(self, data, status_code=200):
        return JSONResponse(content=data, status_code=status_code)
