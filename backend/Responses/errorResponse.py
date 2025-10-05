from pydantic import BaseModel

class errorResponse(BaseModel): 
    status : int
    message : str