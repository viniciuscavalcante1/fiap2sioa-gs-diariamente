from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
def index(request: Request,
          email=Query(...)):
    from server.routes.login import usuario_autenticado
    from server.routes.login import email_usuario
    if usuario_autenticado:
        if email_usuario == email:
            context = {'request': request}
            return templates.TemplateResponse('diario.html', context, status_code=200)
        else:
            # TODO: trocar esse HTTPException por uma página bonitinha de erro
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


@router.post("/")
def diario_post(request: Request,
                titulo: str = Form(...),
                humor: int = Form(...),
                conteudo: str = Form(...),
                momento_feliz: str = Form(...),
                email=Query(...)):
    print(f"titulo: {titulo}\nhumor: {humor}\nconteudo: {conteudo}\nmomento_feliz: {momento_feliz}")
    return RedirectResponse(url=f"/diario?email={email}", status_code=303)
