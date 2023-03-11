import openai

from app.core.config import openai_apikey


openai.api_key = openai_apikey

def ai_response(prompt: str = 'Qué servicios ofrece T-learning'): 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response