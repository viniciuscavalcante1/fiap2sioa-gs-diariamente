from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server.routes.diario import router as diario_router
from server.routes.login import router as login_router
from server.routes.cadastro import router as cadastro_router
from server.routes.meditacao import router as meditacao_router
from server.routes.videos_relaxantes import router as videos_router
from pathlib import Path
from fastapi.exceptions import RequestValidationError
from fastapi import Request, status
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI()

app.include_router(login_router, tags=["login"], prefix="/login")
app.include_router(cadastro_router, tags=["cadastro"], prefix="/cadastro")
app.include_router(diario_router, tags=["diario"], prefix="/diario")
app.include_router(meditacao_router, tags=["meditacao"], prefix="/meditacao")
app.include_router(videos_router, tags=["videos_relaxantes"], prefix="/videos-relaxantes")
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     error_messages = []
#     for entry in exc.errors():
#         error_type = entry['type']
#         error_msg = entry['msg']
#         error_loc = entry['loc'][1]
#
#         formatted_message = f"""<p style="margin-left: 50px;">Missing: {error_loc} - Message: {error_msg}</p>"""
#         error_messages.append(formatted_message)
#     result = "".join(error_messages)
#     context = f"""<h2>Data validation error:</h2><br>
#                         <h3>Detail:</h3> <br>{result}<br>
#                      Please go back to the previous page an correct the errors"""
#
#     return templates.TemplateResponse('index-tela-erro.html', {'request': request, 'message': context},
#                                       status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
