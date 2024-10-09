"""Generate text based off of a short string"""

from fastapi import FastAPI
from routers import nlp, image

app = FastAPI()
app.include_router(image.router)
app.include_router(nlp.router)

@app.get("/")
def read_root():
    """Basic Hello World"""
    return {"Hello": "World"}

