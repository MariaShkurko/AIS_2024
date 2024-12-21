from fastapi import FastAPI, HTTPException
import grpc
from grpc import RpcError
from pydantic import BaseModel
from settings import Settings

from pb.auth_pb2 import AuthRequest
from pb.auth_pb2_grpc import AuthStub
from pb.score_pb2 import ScoreRequest
from pb.score_pb2_grpc import ScoreStub


class LoginRequest(BaseModel):
    login: str
    password: str


settings = Settings()

app = FastAPI()

THRESHOLD_SCORE = settings.threshold_score
AUTH_SERVICE_HOST = settings.auth_service_host
AUTH_SERVICE_PORT = settings.auth_service_port
SCORE_SERVICE_HOST = settings.score_service_host
SCORE_SERVICE_PORT = settings.score_service_port

def get_score_grpc(login: str):
    with grpc.insecure_channel(f"{SCORE_SERVICE_HOST}:{SCORE_SERVICE_PORT}") as channel:
        score_client = ScoreStub(channel)
        try:
            response = score_client.Scoring(ScoreRequest(login=login))
            return response.score
        except RpcError:
            return None

def auth_grpc(request: LoginRequest):
    with grpc.insecure_channel(f"{AUTH_SERVICE_HOST}:{AUTH_SERVICE_PORT}") as channel:
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