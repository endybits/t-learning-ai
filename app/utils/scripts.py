import json

import openai
from app.core.config import openai_apikey

openai.api_key = openai_apikey

def ai_response(
    prompt: str = 'Dame un json con títulos de poemas del siglo XVII'
):
    """_summary_: this function use the OpenAI API to get a custom curriculum 
        for diferent companies requirements.

    Args:
        prompt (str, optional): 'Input/query to interact with OpenAI API'.

    Returns:
        json: json object with the requested information.
    """
    prompt = prompt.replace('     ', ' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.2,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = str(response)
    res = response#.replace("'\n", "")
    json_res = json.loads(res)
    text = json_res['choices'][0]['text']
    text = str(text).replace('\n', '').replace('.', '').replace('\\', '') # Cleaning the output before convert to JSON
    print(text)
    json_text = json.loads(text)
    return json_text