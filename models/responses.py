from pydantic import BaseModel


class Body(BaseModel):
    """Basic Body Response"""

    text: str
