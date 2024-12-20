from fastapi import FastAPI, HTTPException
from random import random


app = FastAPI()

@app.get("/score")
def get_score(login: str):
    if not login:
        raise HTTPException(status_code=400, detail="Login is required")

    score = round(random(), 2)
    return { "score": score }