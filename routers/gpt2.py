"""
GPT2 Text Generator
"""

from routers.main import app


@app.post("/generate")
def generate_text():
    """Generate text based off of a short string"""
    return "coming soon"
    
