from fastapi import FastAPI, HTTPException
import grpc
from grpc import RpcError
from pydantic import BaseModel
from settings import settings

from auth_pb2 import AuthRequest
from auth_pb2_grpc import AuthStub
from score_pb2 import ScoreRequest
from score_pb2_grpc import ScoreStub


class LoginRequest(BaseModel):
    login: str
    password: str


app = FastAPI()

THRESHOLD_SCORE = settings.threshold_score
AUTH_SERVICE = settings.auth_service_url
SCORE_SERVICE = settings.score_service_url

def get_score_grpc(login: str):
    with grpc.insecure_channel(SCORE_SERVICE) as channel:
        score_client = ScoreStub(channel)
        try:
            response = score_client.Scoring(ScoreRequest(login=login))
            return response.score
        except RpcError:
            return None

def auth_grpc(request: LoginRequest):
    with grpc.insecure_channel(AUTH_SERVICE) as channel:
        auth_client = AuthStub(channel)
        try:
            response = auth_client.Authentication(AuthRequest(login=request.login, password=request.password))
            return response.can_login
        except RpcError:
            raise HTTPException(status_code=500, detail="Auth service unavailable")

@app.post("/login")
def user_login(request: LoginRequest):
    score = get_score_grpc(request.login)
    if score is None:
        score = THRESHOLD_SCORE + 0.1

    if score < THRESHOLD_SCORE:
        raise HTTPException(status_code=401, detail="This user is banned")

    can_login = auth_grpc(request)
    return can_login
