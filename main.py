'''
$ sudo pip3 install fastapi
$ pip install uvicorn[standard]
$ uvicorn main:app --reload
'''
from typing import Optional

from fastapi import FastAPI

import json

app = FastAPI()

#JSON SCHEME
#[{"student_id":"0000000000",
# "Evaluation 1":{"value":0,
#                 "%":15,
#                 "Description": "Capítulos 1,2,3"
#                 }, 
# ...
# }
#]
with open('calificaciones.json') as json_file:
    db=json.load(json_file)


@app.get("/")
def read_item(student_id: str = ""):
    '''
    http://127.0.0.1:8000/?student_id=1113674432
    '''
    if not student_id:
    	return db
    else:
    	return [ d for d in db if d.get('student_id')==student_id  ]
