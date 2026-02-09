from fastapi import FastAPI
from app.routes import auth , tickets
app = FastAPI()



@app.get('/health')
def health_check():
    return {'message':'Project is Started'}

app.include_router(auth.router, prefix="/auth",tags=["auth"])
app.include_router(tickets.router, prefix="/tickets",tags=["tickets"])
