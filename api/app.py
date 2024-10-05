
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
app = FastAPI()

class Body(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate")
def generate_text(body: Body):
    result = generator(body.text, max_length=35, num_return_sequences=1, truncation=True)
    return result[0]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}