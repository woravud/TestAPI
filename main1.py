
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class chanom(BaseModel):
    name: str 
    description: Optional[str]
    price : float
    star : int 

chanom_menu = [
    {

        'name' : 'chanom-caimook',
        'description' : 'ชานมไข่มุก',
        'price' : 30 ,
        'star': 5
    }, {

        'name' : 'koko',
        'description' : 'โกโก้หวานหอมอร่อย',
        'price' : 25 ,
        'star': 4
    }
]
test = FastAPI()


@test.get('/')
async def root():
    return chanom_menu

@test.get('/chanom/{chanom_id}')
async def chanom_by_id(id: int ):
    chanom = chanom_menu[id-1]
    return chanom
@test.post('/chanom')
async def create_chanom(chanom: chanom):
    chanom = chanom_menu.append(chanom)
    return chanom_menu[-1]

@test.delete('/chanom/{id}')
async def delete_chanom(id : int ):
    chanom = chanom_menu[id - 1]
    chanom_menu.pop(id - 1)
    result = {'msg', f"{chanom['name']} was delete!"}
    return result

@test.put('/chanom/{id}')
async def update_chanom(id : int,chanom:chanom):
    chanom_menu[id - 1].update(**chanom.dict())
    result = {'msg' : f"chanom ID {id} was Update"} 
    return result
