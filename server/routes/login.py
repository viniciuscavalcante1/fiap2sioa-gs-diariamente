import hashlib

from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates

from server.routes.cadastro import arvore_usuarios

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('login.html', context)


@router.post("/")
def login(request: Request,
          email: str = Form(...),
          senha: str = Form(...)):
    usuario_encontrado = arvore_usuarios.buscar_por_email(email)
    if usuario_encontrado is not None:
        senha_hash = hashlib.md5(senha.encode()).hexdigest()
        if senha_hash == usuario_encontrado.senha:
            return "SENHA E USUARIO CORRETO"
        else:
            return "SENHA INCORRETA"
    else:
        return "USUARIO NAO ENCONTRADO"
