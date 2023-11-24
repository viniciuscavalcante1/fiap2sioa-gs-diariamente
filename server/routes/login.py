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
    """
        Autentica um usuário com base no e-mail e senha fornecidos.

        Args:
            email (str): O e-mail do usuário.
            senha (str): A senha do usuário.

        Returns:
            Tuple[bool, str]: Uma tupla indicando se a autenticação foi bem-sucedida e o e-mail do usuário.
        """
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
    """
        Rota para renderizar a página de login.

        Args:
            request (Request): Objeto da requisição FastAPI.

        Returns:
            TemplateResponse: Resposta contendo a página de login renderizada.
        """
    context = {'request': request}
    return templates.TemplateResponse('login.html', context)


@router.post("/")
def login(request: Request,
          email: str = Form(...),
          senha: str = Form(...)):
    """
        Rota para processar o formulário de login.

        Args:
            request (Request): Objeto da requisição FastAPI.
            email (str): O e-mail fornecido no formulário.
            senha (str): A senha fornecida no formulário.

        Returns:
            RedirectResponse: Redireciona para a página do diário se a autenticação for bem-sucedida.

        Raises:
            HTTPException: Retorna um erro 401 se as credenciais forem inválidas.
        """
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
