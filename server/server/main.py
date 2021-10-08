import uvicorn
from fastapi import FastAPI

from .config import JSON_RESPONSE
from .routers import root, token

# Initialize app instance. See config.py for the default_response_class.
app = FastAPI(default_response_class=JSON_RESPONSE)

# Include routers form .routers
app.include_router(root.router)
app.include_router(token.router)


def run_app():
    uvicorn.run("server.main:app", host="0.0.0.0", reload=True)
