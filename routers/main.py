"""Generate text based off of a short string"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Basic Hello World"""
    return {"Hello": "World"}
