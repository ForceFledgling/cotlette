# cotlette/admin.py
from starlette.routing import Mount, Route
from cotlette.app import Cotlette

def admin_app():
    app = Cotlette()

    @app.route("/")
    async def dashboard(request):
        print(111)
        return await app.render_template(request, "admin/dashboard.html", {"title": "Admin Dashboard"})

    return Mount("/admin", app)
