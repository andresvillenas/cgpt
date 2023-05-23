import openai

from config.settings import Config


class GptService:
    def __init__(self):
        config = Config()
        openai.api_key = config.openai.api_key

    def get_response(self, prompt, temperature=0.25, max_tokens=3000):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
