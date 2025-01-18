# app/main.py
import sys
sys.path.append("/Users/vladimir/Desktop/Личное/cotlette")

from cotlette.app import Cotlette
from cotlette.responses import JSONResponse, HTMLResponse


app = Cotlette()


@app.add_route("/", methods=["GET"], summary="Home Route", description="This is the home route.")
async def home(request):
    return JSONResponse({"message": "Welcome to Cotlette!"})

