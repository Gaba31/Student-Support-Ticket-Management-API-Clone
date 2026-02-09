from pydantic import BaseModel

class TicketCreation(BaseModel):
    title : str
    description : str

    

class TicketUpdate(BaseModel):
    priority: str
    status : str
    