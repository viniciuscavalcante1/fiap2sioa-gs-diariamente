"""
Módulo com a rota de ajuda profissional.
"""
from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates

# Criação do router e do diretório de templates Jinja
router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
def ajuda_profissional(request: Request,
                       email=Query(False)):
    """
        Rota da página de ajuda profissional.

        Args:
            request (Request): Objeto da requisição.
            email (str): E-mail do usuário (opcional).

        Returns:
            TemplateResponse: Resposta com a página renderizada.
        """
    if email:
        context = {"request": request, "email": email}
    else:
        context = {"request": request}
    return templates.TemplateResponse('ajuda-profissional.html', context, status_code=200)
