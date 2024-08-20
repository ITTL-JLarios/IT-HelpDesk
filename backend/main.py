from fastapi import FastAPI

from api.security import token
from api.routes import users

app = FastAPI()

app.include_router(token.router)
app.include_router(users.router)