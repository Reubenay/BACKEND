from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
app = FastAPI(title="Simple FastAPI App", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI Application"}

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))

    # host = os.getenv("host", "127.0.0.1")
    # port = int(os.getenv("port", "8000"))

    # print(f"Starting server on {host}:{port}")
    # uvicorn.run(app, host=host, port=port)
