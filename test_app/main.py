import sys
sys.path.append("/Users/vladimir/Desktop/Личное/cotlette")
import uvicorn

from cotlette.app import Cotlette
from cotlette.core.responses import JSONResponse, HTMLResponse

from cotlette.core.templating import render_template

router = Cotlette()

@router.add_route("/", methods=["GET"], summary="Home Route", description="This is the home route.")
async def home(request):
    # return await render_template(request=request, name="admin/basic-table.html", context={})
    # return await render_template(request=request, name="admin/blank.html", context={})
    # return await render_template(request=request, name="admin/calendar.html", context={})
    # return await render_template(request=request, name="admin/charts.html", context={})
    # return await render_template(request=request, name="admin/chat.html", context={})
    # return await render_template(request=request, name="admin/compose.html", context={})
    return await render_template(request=request, name="admin/datatable.html", context={})
    # return await render_template(request=request, name="admin/email.html", context={})
    # return await render_template(request=request, name="admin/forms.html", context={})
    # return await render_template(request=request, name="admin/google-maps.html", context={})
    # return await render_template(request=request, name="admin/signin.html", context={})
    # return await render_template(request=request, name="admin/signup.html", context={})
    # return await render_template(request=request, name="admin/ui.html", context={})
    # return await render_template(request=request, name="admin/vector-maps.html", context={})

@router.add_route("/auth/users", methods=["GET"], summary="Home Route", description="This is the home route.")
async def home(request):
    return await render_template(request=request, name="test.html", context={})

if __name__ == "__main__":
    uvicorn.run(
        'main:router',
        host="127.0.0.1",
        port=8000,
        reload=True,
        lifespan="off"
    )