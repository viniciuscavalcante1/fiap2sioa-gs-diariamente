from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates
import hashlib

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
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    print(f"Nome: {nome}\t E-mail: {email}\t Senha: {senha_hash}")
    print(hash(senha) == hash(senha))
    return request.json
