"""
GPT2 Text Generator
"""

from fastapi import Depends, HTTPException, APIRouter, FastAPI

router = APIRouter(
    prefix="/image",
    tags=["Image"]
)


@router.post("/generate")
def generate_text():
    """Generate text based off of a short string"""
    return "coming soon"
    
