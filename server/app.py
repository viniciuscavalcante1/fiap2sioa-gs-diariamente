"""
Configuração do aplicativo FastAPI para fornecer rotas para diferentes partes da aplicação.

- `/login`: Rota para autenticação de usuários.
- `/cadastro`: Rota para cadastro de usuários.
- `/diario`: Rota do diário.
- `/meditacao`: Rota para a página de meditação.
- `/videos-relaxantes`: Rota para a página de vídeos.
- `/ajuda-profissional`: Rota para a página de ajuda profissional.
- `/index`: Rota para a página inicial.

O diretório "static" é montado para fornecer arquivos estáticos (css, imagens e áudios).
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server.routes.diario import router as diario_router
from server.routes.login import router as login_router
from server.routes.cadastro import router as cadastro_router
from server.routes.meditacao import router as meditacao_router
from server.routes.videos_relaxantes import router as videos_router
from server.routes.ajuda_profissional import router as ajuda_profissional_router
from server.routes.index import router as index_router
from pathlib import Path
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI()

app.include_router(login_router, tags=["login"], prefix="/login")
app.include_router(cadastro_router, tags=["cadastro"], prefix="/cadastro")
app.include_router(diario_router, tags=["diario"], prefix="/diario")
app.include_router(meditacao_router, tags=["meditacao"], prefix="/meditacao")
app.include_router(videos_router, tags=["videos_relaxantes"], prefix="/videos-relaxantes")
app.include_router(ajuda_profissional_router, tags=["ajuda_profissional"], prefix="/ajuda-profissional")
app.include_router(index_router, tags=["index"])

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)
