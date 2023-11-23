import hashlib
from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException, Header
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from server.routes.cadastro import arvore_usuarios

router = APIRouter()
templates = Jinja2Templates(directory='templates')
usuario_autenticado = False
email_usuario = None


def autenticar_usuario(email, senha):
    usuario_encontrado = arvore_usuarios.buscar_por_email(email)
    if usuario_encontrado is not None:
        senha_hash = hashlib.md5(senha.encode()).hexdigest()
        if senha_hash == usuario_encontrado.senha:
            return True, email
        else:
            return False, "SENHA INCORRETA"
    else:
        return False, "USUARIO NAO ENCONTRADO"


@router.get("/")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('login.html', context)


@router.post("/")
def login(request: Request,
          email: str = Form(...),
          senha: str = Form(...)):
    global usuario_autenticado
    global email_usuario
    usuario_autenticado, email_usuario = autenticar_usuario(email, senha)
    if usuario_autenticado:
        response = RedirectResponse(
            url=f"/diario?email={email}",
            status_code=status.HTTP_302_FOUND)
        return response
    else:
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
