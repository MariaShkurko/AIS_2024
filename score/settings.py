from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    score_service_host: str = "localhost"
    score_service_port: str = "50052"