from fastapi import APIRouter
from ...authentication.supa_auth import get_current_user,get_current_session

import time
from fastapi import FastAPI, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="frontend/static/templates")

import supabase

router = APIRouter()

@router.get("/home", response_class=HTMLResponse)
async def home_page(request: Request):
    user = get_current_session() 
    print('found user')

    if not user:
        response = RedirectResponse(url="/login", status_code=303)
        return response

    context = {
        "request": request,
        "data": user,
        "title": "Home Page",
        "content_template": "arranged_template.html",  # Specify the default template to include
    }

    return templates.TemplateResponse("home.html", context)




@router.get("/chartdata")
async def read_users():
    print('fetching chart data')
    user=get_current_user()

    preloaded_js=[
    {"timestamp": "2023-01-01", "value": 10},
    {"timestamp": "2023-01-02", "value": 15},
    {"timestamp": "2023-01-03", "value": 20},
    {"timestamp": "2023-01-04", "value": 15}
    ]
    
    if not user:
        return [{"error": "Failed to load, not authenticated"}]
    else:
        return preloaded_js
