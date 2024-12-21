from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    auth_service_host: str = "localhost"
    auth_service_port: str = "50051"