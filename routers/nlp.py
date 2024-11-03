"""
NLP Related Routes
"""

from fastapi import Depends, HTTPException, APIRouter, FastAPI, Request
from fastapi.security.http import HTTPAuthorizationCredentials
from nlp.text_generator import TextGenerator
from config import nlp_model
from models.requests import Body
from auth.bearer import CustomHTTPBearer

router = APIRouter(prefix="/nlp", tags=["NLP"])

security = CustomHTTPBearer()

generator = TextGenerator(nlp_model)


@router.post("/generate")
def generate_text(
    request: Request,
    body: Body,
    authorization: HTTPAuthorizationCredentials = Depends(security),
):
    """Generate text based off of a short string"""
    return generator.generate_text(body.text)
    
@router.post("/summerize")
def generate_text(request: Body):
    """Summerize text"""
    return "coming soon"
