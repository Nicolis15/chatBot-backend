from backend.Responses.errorResponse import errorResponse
from backend.Responses.succesResponse import succesResponse
from backend.Model.modelImplementation import ModelImplementation
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI



app = FastAPI()  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def chatBot(prompt):
    try:
        response = ModelImplementation.runModel(prompt)
        message = succesResponse(status=200, message=response)
        return message
    
    except Exception as e:
        error = errorResponse(status=500, message=str(e))
        return error
