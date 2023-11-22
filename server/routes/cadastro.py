from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')

@router.get("/")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('cadastro.html', context)

@router.post("/")
def cadastro(request: Request,
             nome: str = Form(...),
             email: str = Form(...),
             senha: str = Form(...)):
    print(f"Nome: {nome}\t E-mail: {email}\t Senha: {hash(senha)}")
    print(hash(senha) == hash(senha))
    return request.json
