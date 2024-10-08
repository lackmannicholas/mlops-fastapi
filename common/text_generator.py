from transformers import pipeline


class TextGenerator:
    def __init__(self, model_name: str) -> None:
        self.model = model_name
        self.generator = pipeline("text-generation", model=model_name)

    def generate_text(self, text: str):
        """Generate text based off of a short string"""
        result = self.generator(
            text, max_length=35, num_return_sequences=1, truncation=True
        )
        return result[0]
