from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
# TODO: adicionar entradas em json
def index(request: Request):
    from server.routes.login import usuario_autenticado
    if usuario_autenticado:
        context = {'request': request}
        return templates.TemplateResponse('diario.html', context)
    else:
        response = RedirectResponse(
            url=f"/login",
            status_code=status.HTTP_302_FOUND)
        return response
