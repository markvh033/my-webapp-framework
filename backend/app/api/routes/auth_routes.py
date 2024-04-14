# app/routes/auth_routes.py

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse
from ...authentication.supa_auth import authenticate_user,sign_in_user,sign_out_user

router = APIRouter()

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if not user:
        return JSONResponse(status_code=400, content={"message": "Incorrect username or password"})
    print('logging in')
    response = RedirectResponse(url="/home", status_code=303)
    return response

@router.get("/signout")
async def signout(request: Request):
    sign_out_user()
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie(key="sb:token")
    return response