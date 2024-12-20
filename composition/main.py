from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    threshold_score: float = 0.5


settings = Settings()

app = FastAPI()

AUTH_SERVICE_URL = "http://localhost:8001/auth"
SCORE_SERVICE_URL = "http://localhost:8002/score"

class LoginRequest(BaseModel):
    login: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    score_response = requests.get(f"{SCORE_SERVICE_URL}?login={request.login}")
    if score_response.status_code != 200:
        score = settings.threshold_score + 0.1
    else:
        score = score_response.json().get("score")

    if score < settings.threshold_score:
        raise HTTPException(status_code=401, detail="This user is banned")

    auth_response = requests.post(AUTH_SERVICE_URL, json={"login": request.login, "password": request.password})
    if auth_response.status_code != 200:
        raise HTTPException(status_code=auth_response.status_code, detail=auth_response.json())

    can_login = auth_response.json().get("can_login")
    return can_login