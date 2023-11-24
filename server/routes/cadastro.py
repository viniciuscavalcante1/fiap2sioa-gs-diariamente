import json
from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from models.Usuario import Usuario
import hashlib
from utils.ArvoreAVL import ArvoreAVL

router = APIRouter()
templates = Jinja2Templates(directory='templates')


def carregar_dados_json(arquivo):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def salvar_dados_json(arquivo, dados):
    with open(arquivo, 'w') as file:
        json.dump(dados, file)


def json_usuarios_para_arvore_avl(json_usuarios, arvore_usuarios):
    for dado_usuario in json_usuarios.values():
        usuario = Usuario(dado_usuario["nome"], dado_usuario["email"], dado_usuario["senha"])
        arvore_usuarios.inserir_dados(usuario)
    return arvore_usuarios

JSON_USUARIOS_PATH = "data/usuarios.json"
arvore_usuarios = ArvoreAVL()
json_usuarios = carregar_dados_json(JSON_USUARIOS_PATH)
arvore_usuarios = json_usuarios_para_arvore_avl(json_usuarios, arvore_usuarios)

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
    json_usuarios[email] = usuario.dict()
    salvar_dados_json(JSON_USUARIOS_PATH, json_usuarios)
    response = RedirectResponse(
        url=f"/login",
        status_code=status.HTTP_302_FOUND)
    return response
