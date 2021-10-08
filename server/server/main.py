import uvicorn
from fastapi import FastAPI

from .config import JSONresponse
from .routers import root

# Initialize app instance. See config.py for the default_response_class.
app = FastAPI(default_response_class=JSONresponse)
app.include_router(root.router)


def run_app():
    uvicorn.run(app, host="0.0.0.0")
