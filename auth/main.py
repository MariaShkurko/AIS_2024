from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

USER_DB = {
    "user1": "Qweasd123",
    "user2": "Rtyfgh456",
    "user3": "Uiojkl789",
}

class AuthRequest(BaseModel):
    login: str
    password: str


@app.post("/auth")
def auth(request: AuthRequest):
    if not request.login or not request.password:
        raise HTTPException(status_code=400, detail="Login and password are required")

    if request.login in USER_DB and USER_DB[request.login] == request.password:
        return { "can_login": True }
    return { "can_login": False }