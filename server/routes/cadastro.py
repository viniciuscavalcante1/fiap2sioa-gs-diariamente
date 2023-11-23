from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from models.Usuario import Usuario
import hashlib
from utils.ArvoreAVL import ArvoreAVL

router = APIRouter()
templates = Jinja2Templates(directory='templates')
arvore_usuarios = ArvoreAVL()

@router.get("/")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('cadastro.html', context)

@router.post("/")
def cadastro(request: Request,
             nome: str = Form(...),
             email: str = Form(...),
             senha: str = Form(...)):
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    usuario = Usuario(nome, email, senha_hash)
    arvore_usuarios.inserir_dados(usuario)
    arvore_usuarios.imprimir_arvore()
    response = RedirectResponse(
        url=f"/login",
        status_code=status.HTTP_302_FOUND)
    return response