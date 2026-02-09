from fastapi import APIRouter

from datetime import datetime, timedelta
from jose import jwt,JWTError
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
ALG  = os.getenv("ALG")
TIME = int(os.getenv("TIME"))



tickets = APIRouter()

def encode_data(data:dict):
    payload = data.copy()
    payload["exp"] = datetime.now() + timedelta(minutes=TIME)
    token = jwt.encode(payload, key=API_KEY, algorithm=ALG)
    return token


def decode_data(token : str):
     try:
         return jwt.decode(token,API_KEY,algorithms=[ALG])
     except JWTError:
         return {
             "success": False,
             "message": "Invalid Token"
         }


