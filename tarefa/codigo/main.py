#PROJETO EM BETA
#imports
import pandas as pd
import pickle
from fastapi import FastAPI
import requests

import requests
response = requests.get("https://github.com/Foliver335/treinamento-dia-04-08-Foliver33/tree/master/tarefa/codigo/model")
print(response)
#200 é bom, 401 é ruim

app = FastAPI()
@app.post('/model')
# Coloque seu codigo na função abaixo

def titanic(Sex:int ,Age: float,Lifeboat: int,Pclass:int):
#RB significa que o arquivo será aberto e lido em binarios
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

   response.status_code = status.HTTP_200_OK
    return {
        "survived": bool(titanic.predict([[Sex, Age, Lifeboat, Pclass]])),
        "status": response.status_code,
        "message": "  "
 }


@app.get('/model')
def get():
    return {'hello': 'test'}
