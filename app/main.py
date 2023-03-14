import json

from fastapi import FastAPI
from fastapi import Query

from app.utils.scripts import ai_response



app = FastAPI()

@app.get('/')
def home():
    prompt = """Crea una malla curricular de cursos para estas competencias corporativas 
                y organízala por niveles de cargo: Trabajo en equipo, ofimática y liderazgo. 
                Escribe el resultado en notación JSON"""
    response = ai_response(prompt)
    return {'t_learning_ai_response': response}


@app.get('/ai')
def get_custom_query(
    prompt: str = Query(..., example="Dame un json con canciones vallenatas")
):
    response = ai_response(prompt)
    return {'t_learning_ai_response': response}


