# app/main.py
import sys
sys.path.append("/Users/vladimir/Desktop/Личное/cotlette")

from cotlette.app import Cotlette

app = Cotlette()


@app.route("/")
async def home(request):
    # Убедитесь, что render_template вызывается с await
    return await app.render_template(request, "base.html", {"title": "Home"})


