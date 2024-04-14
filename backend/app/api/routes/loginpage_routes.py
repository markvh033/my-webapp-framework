
from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse
from ...authentication.supa_auth import authenticate_user,sign_in_user,sign_out_user,force_sign_in_for_testing,get_current_session
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from starlette.responses import FileResponse 


router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):

    force_sign_in_for_testing()

    user = get_current_session()
    if user:
        return RedirectResponse(url="/home")

 
    return FileResponse("frontend/static/templates/login.html")
