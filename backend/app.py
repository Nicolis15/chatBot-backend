from backend.Responses.errorResponse import errorResponse
from backend.Responses.succesResponse import succesResponse
from fastapi import FastAPI


app = FastAPI()  

@app.get("/")
def chatBot(prompt):
    try:
        message = succesResponse(status=200, message=prompt)
        return message
    
    except Exception as e:
        error = errorResponse(status=500, message=str(e))
        return error
