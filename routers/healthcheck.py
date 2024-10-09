"""
Health Check Routes
"""

from fastapi import APIRouter
from routers import nlp, image

router = APIRouter()

@router.get("/")
def read_root():
    """Basic Health Check"""
    return {"status": "ok"}

