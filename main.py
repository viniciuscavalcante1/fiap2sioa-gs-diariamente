import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter, Request, status, Form, Query, Response, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse, StreamingResponse
from datetime import datetime, date, time, timedelta
from pydantic import EmailStr
from typing import Optional, List, Union, Annotated
from fastapi.templating import Jinja2Templates
from zoneinfo import ZoneInfo
import io
import json

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)