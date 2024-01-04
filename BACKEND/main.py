from fastapi import FastAPI
from . import models
from .database import engine
from .routers import login, user, wine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(user.router)
app.include_router(login.router)
app.include_router(wine.router)


@app.get("/") # Decorator that apply to the function below, allowing the *magic*
def root():
    return {"message": "Home Page"}