import json
import os.path
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
    """
        Rota para renderizar a página principal do diário.

        Args:
            request (Request): Objeto da requisição FastAPI.
            email (str): O e-mail do usuário.

        Returns:
            TemplateResponse: Resposta contendo a página renderizada do diário.
        """
    from server.routes.login import usuario_autenticado
    from server.routes.login import email_usuario
    if usuario_autenticado:
        if email_usuario == email:
            context = {'request': request, 'email': email}
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
    """
        Rota para lidar com o envio de uma nova entrada no diário.

        Args:
            request (Request): Objeto da requisição FastAPI.
            titulo (str): O título da entrada.
            humor (int): O nível de humor da entrada.
            conteudo (str): O conteúdo da entrada.
            momento_feliz (str): Um momento feliz da entrada.
            email (str): O e-mail do usuário.

        Returns:
            RedirectResponse: Redireciona para a página do diário após o envio da entrada.
        """
    entrada_diario = {
        "email": email,
        "titulo": titulo,
        "humor": humor,
        "conteudo": conteudo,
        "momento_feliz": momento_feliz,
        "timestamp": datetime.now().isoformat()
    }
    with open("data/entradas_diario.json", "r") as arquivo:
        dados = json.load(arquivo)
        if email in dados:
            dados[email].append(entrada_diario)
        else:
            dados[email] = [entrada_diario]

    with open("C:\\Users\\vinicius.cavalcante\\Documents\\GitHub\\fiap\\fiap2sioa-gs-diariamente\\data"
              "\\entradas_diario.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=2)

    return RedirectResponse(url=f"/diario?email={email}", status_code=303)


def quicksort_entradas(entradas_usuario):
    """
        Implementa o algoritmo de ordenação quicksort para ordenar entradas do diário por timestamp.

        Args:
            entradas_usuario (list): Lista de entradas do diário de um usuário.

        Returns:
            list: Lista ordenada de entradas do diário.
        """
    if len(entradas_usuario) <= 1:
        return entradas_usuario

    pivot = entradas_usuario[len(entradas_usuario) // 2]['timestamp']
    left = [x for x in entradas_usuario if x['timestamp'] > pivot]
    middle = [x for x in entradas_usuario if x['timestamp'] == pivot]
    right = [x for x in entradas_usuario if x['timestamp'] < pivot]

    return quicksort_entradas(left) + middle + quicksort_entradas(right)


@router.get("/entradas")
def index(request: Request,
          email=Query(...)):
    """
        Rota para renderizar a página de entradas do diário.

        Args:
            request (Request): Objeto da requisição FastAPI.
            email (str): O e-mail do usuário.

        Returns:
            TemplateResponse: Resposta contendo a página renderizada de entradas do diário.
        """
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
                entradas_usuario = quicksort_entradas(entradas_usuario)
                return templates.TemplateResponse(
                    "entradas.html",
                    {"request": request, "email": email, "entradas_usuario": entradas_usuario}
                )
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
