# app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    username: str
    password: str

@app.get("/")
def root():
    return {"hello": "world"}

@app.post("/login")
def login(data: Login):
    # pretend login endpoint: receives JSON {username, password}
    return {"status": "ok", "user": data.username}
