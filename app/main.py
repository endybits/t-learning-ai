import json

from fastapi import FastAPI
from app.utils.scripts import ai_response

app = FastAPI()

@app.get('/')
def home():
    prompt = """Crea una malla curricular de cursos para estas competencias corporativas 
                y organízala por niveles de cargo: Trabajo en equipo, ofimática y liderazgo. 
                Escribe el resultado en notación JSON"""
    response = ai_response()
    return {'t_learning_ai_response': response}