from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates

from server.routes.login import usuario_autenticado

router = APIRouter()
templates = Jinja2Templates(directory='templates')

@router.get("/")
def index(request: Request):
    if usuario_autenticado:
        context = {'request': request}
        return templates.TemplateResponse('diario.html', context)
    else:
        raise HTTPException(
            status_code=403,
            detail="Sem permissão",
            headers={"WWW-Authenticate": "Bearer"}
        )