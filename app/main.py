# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["root"])
async def root():
    print("Here")
    return {"message": "Hello World"}