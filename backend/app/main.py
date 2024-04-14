from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from ..app.api.routes import homepage_routes,loginpage_routes, auth_routes,user_settings_routes,inbox_routes,notes_routes
from .authentication.supa_auth import force_sign_in_for_testing


app = FastAPI()
app.include_router(homepage_routes.router)
app.include_router(loginpage_routes.router)
app.include_router(auth_routes.router)
app.include_router(user_settings_routes.router)
app.include_router(inbox_routes.router)
app.include_router(notes_routes.router)




app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/static/templates")

@app.get("/")
async def root(request: Request):

    force_sign_in_for_testing()

    if "user" in request.cookies: 
        return RedirectResponse(url="/home")
    else:
        return RedirectResponse(url="/login")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, debug=True)