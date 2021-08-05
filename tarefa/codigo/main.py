# imports
import pandas as pd
import pickle
from fastapi import FastAPI
import requests
import os

import requests

response = requests.get("https://github.com/Foliver335/treinamento-dia-04-08-Foliver33/tree/master/tarefa/codigo/model")
print(response)
# 200 é bom, 401 é ruim

import pickle
from fastapi import FastAPI, Response, status

app = FastAPI()


@app.post('/model')

async def titanic(Sex: int, Age: float, Lifeboat: int, Pclass: int, response: Response):
    # rb= ler em binarios
    with open('Titanic.pkl', 'rb') as fid:
        titanic = pickle.load(fid)

        response.status_code = status.HTTP_200_OK
    return {
        "survived": bool check (titanic.predict([[Sex, Age, Lifeboat, Pclass]])) = true;
        bool check = true;
        Console.WriteLine(check ? "alive" : "not alive");
        Console.WriteLine(false ? "alive" : "not alive");  
        
        "status": response.status_code,
        "message": ' '
    }


@app.get('/model')
def get():
    return {'hello': 'test'}
