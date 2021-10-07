# Evaluación 2021-1
Abrir en Firefox y hacer click en "Colapse All" para mejorar la visulación:
* [http://clustercien.udea.edu.co:8000/](http://clustercien.udea.edu.co:8000/)

Abrir en Firefox con su identificación, por ejemplo: después de abrir el link cambiar el número al final: `0000000000`, por su identificación
* [http://clustercien.udea.edu.co:8000/?student_id=0000000000](http://clustercien.udea.edu.co:8000/?student_id=0000000000)
  * Powered by [FastAPI](https://fastapi.tiangolo.com/), see [`main.py`](./main.py)

Descarga JSON:
* [./calificaciones.json](./calificaciones.json)
o con pandas
```pyhon
import pandas as pd
df=pd.read_json('https://raw.githubusercontent.com/ComputationalMethods/Evaluacion_2021-1/main/calificaciones.json')
```

See official repo at:

https://github.com/restrepo/examenes/tree/master/ComputationalMethods

