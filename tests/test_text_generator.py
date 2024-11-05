import pytest
from transformers import pipeline
from nlp.text_generator import TextGenerator


@pytest.fixture
def mock_pipeline(mocker):
    return mocker.patch("nlp.text_generator.pipeline")


@pytest.fixture
def text_generator(mock_pipeline):
    mock_pipeline.return_value = (
        lambda text, max_length, num_return_sequences, truncation: [
            {"generated_text": f"sample generated text {i}"}
            for i in range(num_return_sequences)
        ]
    )

    return TextGenerator(model_name="gpt2")


def test_generate_text_success(text_generator):
    result = text_generator.generate_text("Hello")
    assert result[0]["generated_text"] == "sample generated text 0"


def test_generate_text_empty_string(text_generator):
    with pytest.raises(ValueError, match="text is empty. Value is required."):
        text_generator.generate_text("")


def test_generate_text_multiple_sentences(text_generator):
    result = text_generator.generate_text("Hello", num_char=35, num_sequences=3)
    assert len(result) == 3
    assert result[0]["generated_text"] == "sample generated text 0"
    assert result[1]["generated_text"] == "sample generated text 1"
    assert result[2]["generated_text"] == "sample generated text 2"
