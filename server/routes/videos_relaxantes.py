from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
def videos(request: Request,
           email=Query(False)):
    """
        Rota para renderizar a página de vídeos relaxantes.

        Args:
            request (Request): Objeto da requisição FastAPI.
            email (str, optional): O e-mail do usuário (opcional). Se fornecido, será incluído no contexto.

        Returns:
            TemplateResponse: Resposta contendo a página de vídeos relaxantes renderizada.

        Note:
            Se um e-mail for fornecido, ele será incluído no contexto da página.
        """
    if email:
        context = {"request": request, "email": email}
    else:
        context = {"request": request}
    return templates.TemplateResponse('videos-relaxantes.html', context, status_code=200)
