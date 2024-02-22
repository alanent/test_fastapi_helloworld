from fastapi import FastAPI
from uvicorn import run
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
