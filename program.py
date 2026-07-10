from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working"}

@app.get("/add")
def add(a: int,b: int):
    return a+b

@app.get("/subtract")
def subtract(a: int,b: int):
    return a-b

