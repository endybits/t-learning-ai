import json

from fastapi import FastAPI
from app.utils.scripts import ai_response

app = FastAPI()

@app.get('/')
def home():
    prompt = "Crea una malla curricular de cursos para estas competencias corporativas y organízala por niveles de cargo: Trabajo en equipo, ofimática y liderazgo. Escribe el resultado en notación JSON"
    res = ai_response(prompt)
    print(type(res))
    json_res = json.loads(str(res))
    response = json_res['choices'][0]['text']
    #print(type(response))
    return {'t_learning_ai_response': response}