import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def my_function():
    return 'PROYECTO INDIVIDUAL Nº1 Machine Learning Operations (MLOps)'

@app.get('/')
def determinar_efectivo():
    