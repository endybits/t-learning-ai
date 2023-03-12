import json

import openai

from app.core.config import openai_apikey


openai.api_key = openai_apikey

def ai_response(
    prompt: str = 'Qué servicios ofrece T-learning'
): 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.2,
        max_tokens=768,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = str(response)
    res = response#.replace("'\n", "")
    json_res = json.loads(res)
    text = json_res['choices'][0]['text']
    print(text)
    text = str(text).replace('\n', '').replace('.', '').replace('\\', '')
    json_text = json.loads(text)
    return json_text