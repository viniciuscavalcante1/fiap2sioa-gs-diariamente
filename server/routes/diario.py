from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
# TODO: adicionar entradas em json
def index(request: Request,
          email=Query(...)):
    from server.routes.login import usuario_autenticado
    from server.routes.login import email_usuario
    if usuario_autenticado:
        if email_usuario == email:
            context = {'request': request}
            return templates.TemplateResponse('diario.html', context, status_code=200)
        else:
            raise HTTPException(
                status_code=403,
                detail="Sem permissão",
                headers={"WWW-Authenticate": "Bearer"}
            )
    else:
        response = RedirectResponse(
            url=f"/login",
            status_code=status.HTTP_302_FOUND)
        return response
