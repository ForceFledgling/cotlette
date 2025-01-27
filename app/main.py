# app/main.py
import sys
sys.path.append("/Users/vladimir/Desktop/Личное/cotlette")
import uvicorn

from cotlette.app import Cotlette
from cotlette.responses import JSONResponse, HTMLResponse


app = Cotlette()

@app.add_route("/", methods=["GET"], summary="Home Route", description="This is the home route.")
async def home(request):
    return JSONResponse({"message": "Welcome to Cotlette!"})

if __name__ == "__main__":
    uvicorn.run(
    'main:app',
    host="127.0.0.1",
    port=8000,
    reload=True,
)