from starlette.templating import Jinja2Templates as Jinja2Templates  # noqa

from cotlette.app import Cotlette


router = Cotlette()


async def render_template(request, name: str, context: dict = {}):
    return router.templates.TemplateResponse(
        request=request, name=name, context={}
    )
