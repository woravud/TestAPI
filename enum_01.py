from fastapi import FastAPI
from enum import Enum, IntEnum

class Users(IntEnum, Enum):
  mrchoke = 1
  taz = 2
  tony = 3

app = FastAPI()

@app.get("/users/{info}")
async def get_username(info: Users):
 return {"id": info.value, "username": info.name }