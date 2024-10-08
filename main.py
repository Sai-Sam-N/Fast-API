# Library Imports
import uvicorn #ASGI
from fastapi import FastAPI

# Create the app object
app = FastAPI()

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message' : 'Hello, stranger'}

# Route with a single parameter, returns the parameter within a message
# Located at : http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str): #When this API is hit, it expects a string input which will be stored in the parameter 'name'
    return {'Welcome' : f'{name}'}

# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


#uvicorn main:app --reload
#uvicorn <python filename w/o .py>:<the name of the FastAPI app variable. Here, app=FastAPI()> --reload