import uvicorn
from fastapi import FastAPI
from bankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

# Create the app object
app = FastAPI()
pickle_in - open(r'C:\Users\SAN0001\Documents\Appu\05 PythonGit\Fast-API\classifier.pkl', 'rb') #open the pickle file in read mode
classifier = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message' : 'Hello There'}

@app.get('/{name}')
def