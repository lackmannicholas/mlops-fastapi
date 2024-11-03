from transformers import pipeline


class TextSummerizer:
    def __init__(self, model_name: str) -> None:
        self.model = model_name
        self.summerizer = pipeline("summarization", model=model_name)

    def generate_text(self, text: str):
        """Summerize text based off of a short string"""
        result = self.summerizer(text)
        return result[0]
