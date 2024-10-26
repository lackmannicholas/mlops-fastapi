"""
NLP Related Routes
"""

from fastapi import Depends, HTTPException, APIRouter, FastAPI
from nlp.text_generator import TextGenerator
from config import nlp_model
from models.requests import Body

router = APIRouter(
    prefix="/nlp",
    tags=["NLP"]
)

print(nlp_model)

generator = TextGenerator(nlp_model)

@router.post("/generate")
def generate_text(request: Body):
    """Generate text based off of a short string"""
    
    return generator.generate_text(request.text)
    
@router.post("/summerize")
def generate_text(request: Body):
    """Summerize text"""
    return "coming soon"
