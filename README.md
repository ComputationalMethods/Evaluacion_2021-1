# Evaluación 2021-1
Abrir en Firefox y hacer click en "Colapse All" para mejorar la visualización:
* [http://clustercien.udea.edu.co:8000/](http://clustercien.udea.edu.co:8000/)

Abrir en Firefox con su identificación: después de abrir el siguiente link cambiar el número al final: `0000000000`, por su identificación
* [http://clustercien.udea.edu.co:8000/?student_id=0000000000](http://clustercien.udea.edu.co:8000/?student_id=0000000000)
  * Powered by [FastAPI](https://fastapi.tiangolo.com/), see [`main.py`](./main.py)

O use la documentación del API, a continuación, desplegando el botón "GET" y despúes de hacer click sobre el botón "Try it out", introducir la identificación en la caja "`student_id`" y pulsar el botón "Execute":
* [http://clustercien.udea.edu.co:8000/docs](http://clustercien.udea.edu.co:8000/docs)

Descarga JSON:
* [./calificaciones.json](https://computationalmethods.github.io/Evaluacion_2021-1/calificaciones.json)

O con pandas
```pyhon
import pandas as pd
df=pd.read_json('https://computationalmethods.github.io/Evaluacion_2021-1/calificaciones.json')
```

See official repo at:

https://github.com/restrepo/examenes/tree/master/ComputationalMethods

## Fast API
See install options and usage at: https://fastapi.tiangolo.com/
```
$ uvicorn main:app --reload --host clustercien.udea.edu.co
```


