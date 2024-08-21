from fastapi import FastAPI

from api.security import token
from api.routes import user, ticket

app = FastAPI()

app.include_router(token.router)
app.include_router(user.router)
app.include_router(ticket.router)