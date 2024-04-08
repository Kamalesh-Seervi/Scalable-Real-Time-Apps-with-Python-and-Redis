import asyncio
from fastapi import FastAPI
from dataclasses import dataclass
from typing import Dict



app = FastAPI()

@dataclass
class data:
    id:int
    name:str
    marks:float
    

users:Dict[int,data]={
    1:data(1,"Kamalesh",85.23),
    2:data(2,"Sumanth",76.45),
    3:data(3,"Ajay",90)
}
# print(users[1])

@app.get("userdata/{user_id}")
async def read_item(user_id: int):
    # for testing purpose i am doing 0.2
    await asyncio.sleep(0.2)
    if user_id in users:
        return {"ok": True, "user": users[user_id]}
    return {"ok": False, "error": "user not there"}