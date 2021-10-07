from fastapi import FastAPI
import uvicorn
from config import JSONresponse

# Initialize app instance. See config.py for the default_response_class.
app = FastAPI(default_response_class=JSONresponse)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
