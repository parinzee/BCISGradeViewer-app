import uvicorn
from fastapi import FastAPI

from .config import JSON_RESPONSE
from .routers import user, token

from .sql import models, database

# Initialize SQL database first.
models.Base.metadata.create_all(bind=database.engine)

# Initialize app instance. See config.py for the default_response_class.
app = FastAPI(default_response_class=JSON_RESPONSE)

# Include routers form .routers
app.include_router(user.router)
app.include_router(token.router)


def run_app():
    uvicorn.run("server.main:app", host="0.0.0.0", reload=True)
