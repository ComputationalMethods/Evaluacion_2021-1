'''
$ sudo pip3 install fastapi
$ pip install uvicorn[standard]
$ uvicorn main:app --reload
'''
from typing import Optional

from fastapi import FastAPI

import requests

import json

app = FastAPI()

file='https://raw.githubusercontent.com/ComputationalMethods/Evaluacion_2021-1/main/calificaciones.json'

#JSON SCHEME
#[{"student_id": str,
# "Evaluation 1":{"value": int,
#                 "%": int,
#                 "Description": str
#                 }, 
# ...
# }
#]

@app.get("/")
def read_item(student_id: str = ""):
    '''
    http://clustercien.udea.edu.co:8000/?student_id=1113674432
    '''
    #Real time JSON file
    r=requests.get(file)
    db=r.json()
    #with open(file) as json_file:
    #   db=json.load(json_file)

    if not student_id:
    	return db
    else:
    	return [ d for d in db if d.get('student_id')==student_id  ]
