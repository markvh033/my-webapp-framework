

from fastapi import APIRouter
from ...authentication.supa_auth import get_current_user, get_current_session

import time
from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse

from fastapi.templating import Jinja2Templates
from ..databases.mongo import connection
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from ...utils.mongo_encoder import object_id_to_str


templates = Jinja2Templates(directory="frontend/static/templates")

router = APIRouter()


@router.get("/notes", response_class=HTMLResponse)
async def notes_page(request: Request):
    user = get_current_session()  
    if not user:
        user=get_current_user()
        return RedirectResponse(url="/login", status_code=303)
    
    #messages=get_inbox_messages(user.user.email)

    context = {
        "request": request,
        "data": user,
        "title": "Notes",
        "content_template": "notes.html",  # Specify the template to include
    }
    return templates.TemplateResponse("home.html", context)