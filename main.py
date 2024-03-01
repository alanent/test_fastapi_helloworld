from fastapi import FastAPI
import tensorflow as tf

app = FastAPI()

@app.get("/")
async def root():
    return {"message": tf.__version__}
