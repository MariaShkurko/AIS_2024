from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    auth_service_host: str = "localhost"
    auth_service_port: str = "50051"
    score_service_host: str = "localhost"
    score_service_port: str = "50052"
    threshold_score: float = 0.5