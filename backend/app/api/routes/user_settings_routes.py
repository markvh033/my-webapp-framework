# user_settings_routes.py

from fastapi import APIRouter, Request, Form,Depends,File, UploadFile,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from ..databases.mongo import connection
from ...authentication.supa_auth import get_current_user,get_current_session
from fastapi.responses import RedirectResponse
from time import time
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Dict,Optional

router = APIRouter()
templates = Jinja2Templates(directory="frontend/static/templates")


fields = ["country", "city", "address", "firstname", "lastname", "receive_emails", "profile_picture"]


@router.get("/user-settings", response_class=HTMLResponse)
async def user_settings(request: Request):
    s=time()
    #user = get_current_user()
    user= get_current_session()
    if not user:
        return RedirectResponse(url="/login")
    e=time()
    print('checked user state in ',e-s)


    settings = connection.framework.user_settings.find_one({"username": user.user.email})


    # Use dictionary comprehension to extract all fields, defaulting to "" if not found
    user_settings = {field: settings.get(field, "") for field in fields}

    # Update the context dictionary directly with the extracted settings
    context = {
        "request": request,
        "data": user,
        "title": "User Settings",
        "content_template": "user_settings.html",  # Specify the template to include
        **user_settings  # Unpack user_settings into the context
    }
    return templates.TemplateResponse("home.html", context)  # Render the home.html template




@router.post("/save_user_settings_old", response_class=HTMLResponse)
async def user_settings(
    country: str = Form(...), 
    city: str = Form(...), 
    address: str = Form(...), 
    profile_picture: UploadFile = File(...),
    email_notifications: Optional[bool] = Form(None)):
    

    user= get_current_session()
    if not user:
        return RedirectResponse(url="/login")
    # Convert inputs to a dictionary
    save_result=None
    
    settings_data = {
        "country": country,
        "city": city,
        "address": address,
        # Assume you're processing or saving the file here and just storing a reference or filename
        "profile_picture": profile_picture.filename,
        "email_notifications": email_notifications if email_notifications is not None else False
    }


    settings = connection.framework.user_settings.find_one({"username": user.user.email})
    if settings:
        # Update the user's settings with the new data
        connection.framework.user_settings.update_one({"username": user.user.email}, {"$set": settings_data})
    else:
        # If settings do not exist, insert new settings along with the username
        connection.framework.user_settings.insert_one({"username": user.user.email, **settings_data})
    

  

    return RedirectResponse(url="/user-settings", status_code=303)


from pydantic import BaseModel
from typing import Dict

# ... existing imports ...

class UserSettings(BaseModel):
    settings: Dict[str, str]

@router.post("/save-user-settings")
async def update_user_settings(settings: UserSettings, request: Request):
    user = get_current_session()
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        # Update the user's settings in MongoDB
        update_result = connection.framework.user_settings.update_one(
            {"username": user.user.email},
            {"$set": settings.model_dump()["settings"]},
            upsert=True
        )
        return JSONResponse(content={"message": "Settings updated successfully"}, status_code=200)
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to update settings")
