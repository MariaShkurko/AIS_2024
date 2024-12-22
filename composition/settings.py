from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Composition App"
    score_service_url: str
    auth_service_url: str
    threshold_score: float

    class Config:
        env_file = ".env"


settings = Settings()