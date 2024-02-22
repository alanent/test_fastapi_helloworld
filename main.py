from fastapi import FastAPI
from uvicorn import run
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
