"""
NLP Related Routes
"""

from fastapi import Depends, HTTPException, APIRouter, FastAPI

router = APIRouter(
    prefix="/nlp",
    tags=["NLP"]
)

@router.post("/generate")
def generate_text():
    """Generate text based off of a short string"""
    return "coming soon"
    
