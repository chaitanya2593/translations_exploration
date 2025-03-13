import pandas as pd
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="Triangle104/EuroLLM-9B-Q8_0-GGUF",
    filename="eurollm-9b-q8_0.gguf",
)


def translate_text(source_lang, target_lang , input_text):
    '''
    This function will translate the input text from source language to target language.
    :param source_lang: Source language
    :param target_lang: Target language
    :param input_text: The text to translate
    :return: The translated text
    '''
    output = llm(
        f"""Translate the following {source_lang} text to {target_lang}. Only return the translated text, nothing else.\n"
        "{source_lang} text: {input_text}r\n"
        "{target_lang}:""",
        max_tokens=200,  # Limit the response length
        stop=["\n"],  # Stops generation at the first newline to avoid extra text
        temperature=0  # Makes the output deterministic
    )
    return output['choices'][0]['text']