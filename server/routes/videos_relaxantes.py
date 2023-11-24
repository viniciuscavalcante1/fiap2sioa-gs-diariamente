from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
def videos(request: Request,
           email=Query(False)):
    if email:
        context = {"request": request, "email": email}
    else:
        context = {"request": request}
    return templates.TemplateResponse('videos-relaxantes.html', context, status_code=200)
