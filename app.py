"""Generate text based off of a short string"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import nlp, image, healthcheck

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(healthcheck.router)
app.include_router(image.router)
app.include_router(nlp.router)
