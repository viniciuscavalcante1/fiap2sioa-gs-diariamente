import json
from datetime import datetime

from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import RedirectResponse, JSONResponse
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
    entrada_diario = {
        "email": email,
        "titulo": titulo,
        "humor": humor,
        "conteudo": conteudo,
        "momento_feliz": momento_feliz,
        "timestamp": datetime.now().isoformat()
    }
    with open("C:\\Users\\vinicius.cavalcante\\Documents\\GitHub\\fiap\\fiap2sioa-gs-diariamente\\data"
              "\\entradas_diario.json", "r") as arquivo:
        dados = json.load(arquivo)
        if email in dados:
            dados[email].append(entrada_diario)
        else:
            dados[email] = [entrada_diario]

    with open("C:\\Users\\vinicius.cavalcante\\Documents\\GitHub\\fiap\\fiap2sioa-gs-diariamente\\data"
              "\\entradas_diario.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=2)

    return RedirectResponse(url=f"/diario?email={email}", status_code=303)


@router.get("/entradas")
def index(request: Request,
          email=Query(...)):
    from server.routes.login import usuario_autenticado
    from server.routes.login import email_usuario
    if usuario_autenticado:
        if email_usuario == email:
            context = {'request': request}
            with open("C:\\Users\\vinicius.cavalcante\\Documents\\GitHub\\fiap\\fiap2sioa-gs-diariamente\\data"
                      "\\entradas_diario.json", "r") as arquivo:
                entradas = json.load(arquivo)
                entradas_usuario = entradas.get(email, [])
                if not entradas_usuario:
                    raise HTTPException(status_code=404, detail="Diário não encontrado")
                return JSONResponse(content=jsonable_encoder(entradas_usuario))
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
