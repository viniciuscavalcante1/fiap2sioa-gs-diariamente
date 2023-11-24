from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
def index_homepage(request: Request,
          email=Query(False)):
    context = {"request": request}
    return templates.TemplateResponse('index.html', context, status_code=200)
