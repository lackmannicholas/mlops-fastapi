from transformers import pipeline


class TextGenerator:
    def __init__(self, model_name: str) -> None:
        self.model = model_name
        self.generator = pipeline("text-generation", model=model_name)

    def generate_text(self, text: str = "", num_sentences: int = 10):
        """Generate text based off of a short string"""

        if(text == ""):
            raise ValueError("text is empty. Value is required.")

        result = self.generator(
            text, max_length=35, num_return_sequences=num_sentences, truncation=True
        )
        return result[0]
