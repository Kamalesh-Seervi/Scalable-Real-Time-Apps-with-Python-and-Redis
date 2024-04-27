import asyncio
from fastapi import FastAPI
from dataclasses import dataclass
from typing import Dict
import requests
import uvicorn


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
async def get_user(user_id: int):
    # for testing purpose i am doing 0.2
    await asyncio.sleep(0.2)
    if user_id in users:
        return {"ok": True, "user": users[user_id]}
    return {"ok": False, "error": "user not there"}

# def get_user_info(user_id: int) -> dict | None:
#     response=requests.get(f"http://127.0.0.1:8000/user/{user_id}").json()
#     return response
    
    
    
    
    
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
    
    
    