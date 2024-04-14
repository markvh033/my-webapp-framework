
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


@router.get("/get-messages")
async def get_messages(request: Request):
    user = get_current_session()

    if user is None:
        return RedirectResponse(url="/login", status_code=303)

    response = connection.framework.inbox.find({"username": user.user.email})

    # Convert MongoDB documents to dicts and ObjectId instances to strings
    messages = [object_id_to_str(document) for document in response]

    # Now it's safe to return messages, as they are serializable to JSON
    return jsonable_encoder(messages)
 


@router.get("/inbox", response_class=HTMLResponse)
async def inbox_page(request: Request):
    user = get_current_session()  
    if not user:
        user=get_current_user()
        return RedirectResponse(url="/login", status_code=303)
    
    #messages=get_inbox_messages(user.user.email)

    context = {
        "request": request,
        "data": user,
        "title": "Inbox",
        "content_template": "inbox.html",  # Specify the template to include
    }
    return templates.TemplateResponse("home.html", context)


outer = APIRouter()

# In your backend routes file

@router.post("/mark-as-read/{message_id}")
async def mark_as_read(message_id: str):
    print(message_id)
    oid = ObjectId(message_id)
    # Update the message in the database and set has_been_read to True
    result=connection.framework.inbox.update_one({"_id": oid}, {"$set": {"has_been_read": True}})
    print(result.raw_result)
    return {"message": "Message marked as read"}

@router.post("/delete-message/{message_id}")
async def delete_message(message_id: str):
    oid = ObjectId(message_id)
    # Update the message in the database and set has_been_deleted to True
    connection.framework.inbox.update_one({"_id": oid}, {"$set": {"has_been_deleted": True}})
    print('deleted')
    return {"message": "Message marked as deleted"}

    