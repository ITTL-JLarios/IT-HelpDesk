from fastapi import FastAPI

from api.security import token

app = FastAPI()

app.include_router(token.router)