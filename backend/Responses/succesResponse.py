from pydantic import BaseModel

class succesResponse(BaseModel):
    status : int
    message : str