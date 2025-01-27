from starlette.responses import JSONResponse as StarletteJSONResponse, HTMLResponse as StarletteHTMLResponse


class JSONResponse(StarletteJSONResponse):
    """Заменяет Starlette JSONResponse для совместимости с Cotlette"""
    pass


class HTMLResponse(StarletteHTMLResponse):
    """Заменяет Starlette HTMLResponse для совместимости с Cotlette"""
    pass
