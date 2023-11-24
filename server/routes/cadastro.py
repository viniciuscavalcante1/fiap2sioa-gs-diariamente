import json
from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from models.Usuario import Usuario
import hashlib
from utils.ArvoreAVL import ArvoreAVL
import time

router = APIRouter()
templates = Jinja2Templates(directory='templates')


def carregar_dados_json(arquivo):
    """
        Carrega dados de um arquivo json.

        Args:
            arquivo (str): Caminho do json.

        Returns:
            dict: Dados json carregados.
        """
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def salvar_dados_json(arquivo, dados):
    """
        Salva dados em um arquivo json.

        Args:
            arquivo (str): Caminho do json.
            dados (dict): Os dados para serem salvos.
        """
    with open(arquivo, 'w') as file:
        json.dump(dados, file)


def json_usuarios_para_arvore_avl(json_usuarios, arvore_usuarios):
    """
        Lê um arquivo json com usuários e alimenta uma árvore AVL.

        Args:
            json_usuarios (dict): Dados do usuário em json.
            arvore_usuarios (ArvoreAVL): Árvore AVL de usuários.

        Returns:
            ArvoreAVL: Árvore AVL com os usuários atualizados..
        """
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
    """
        Rota da página de cadastro.

        Args:
            request (Request): Objeto FastAPI.

        Returns:
            TemplateResponse: Resposta da página renderizada.
        """
    context = {'request': request}
    return templates.TemplateResponse('cadastro.html', context)


@router.post("/")
def cadastro(request: Request,
             nome: str = Form(...),
             email: str = Form(...),
             senha: str = Form(...)):
    """
        Rota para lidar com o cadastro de novos usuários.

        Args:
            request (Request): Objeto FastAPI.
            nome (str): Nome do usuário.
            email (str): E-mail do usuário.
            senha (str): Senha do usuário.

        Returns:
            RedirectResponse: Redireciona para a página de login após o cadastro.
        """
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


def inserir_n_usuarios(n):
    """
        Insere um número n de usuários na Árvore AVL e atualiza o arquivo json depois.

        Args:
            n (int): O número de usuários a serem inseridos.

        Returns:
            str: Mensagem indicando o tempo total de inserção e a média de tempo por usuário.
        """
    inicio_tempo = time.time()
    usuarios_temp = []
    for i in range(n):
        email = str(i) + "@gmail.com"
        usuario = Usuario(nome=str(i), email=email, senha=str(i))
        usuarios_temp.append((email, usuario.dict()))
        arvore_usuarios.inserir_dados(usuario)
    fim_tempo = time.time()
    json_usuarios.update(usuarios_temp)
    salvar_dados_json(JSON_USUARIOS_PATH, json_usuarios)
    return f"O tempo de inserção total para {n} usuários foi de {fim_tempo - inicio_tempo} segundos. Em média, {(fim_tempo - inicio_tempo)/n} segundos por usuário."


print(inserir_n_usuarios(1000))
print(inserir_n_usuarios(10000))
print(inserir_n_usuarios(100000))
