from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "SkyCare Backend is running!"}
