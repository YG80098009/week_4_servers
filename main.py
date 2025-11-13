from typing import Literal
from fastapi import FastAPI,HTTPException
import uvicorn
import json
from pydantic import BaseModel



def main_():
    pass

app = FastAPI()
items = []
url = "http://127.0.0.1:8000/test"

@app.get("/test/") 
def get_name():
    response = {"msg": "hi from test" }
    return response


@app.get("/test/{Avi}") 
def test():
    Response = { "msg": "saved user" } 
    with open("names.txt","a") as f:
        f.write("Avi")
    return Response

list_AB = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
class Item_k(BaseModel):
    text: str
    offset: int
    mode: Literal["encrypt", "decrypt"]



def encrypted(item: Item_k):
    new_list = []
    for char in item.text:
        for i in range(len(list_AB)):
            if list_AB[i] == char:
                new_list.append(list_AB[(i + item.offset) % len(list_AB)])
    responce = ""
    for letter in new_list:
        responce += letter
    return {"encrypted_text": responce} 

def decrypted(item: Item_k):
    new_list = []
    for char in item.text:
        for i in range(len(list_AB)):
            if list_AB[i] == char:
                new_list.append(list_AB[(i - item.offset) % len(list_AB)])
    responce = ""
    for letter in new_list:
        responce += letter
    return {"decrypted_text": responce} 

@app.post("/caesar")
def check_mode(item: Item_k):
    if item.mode == "encrypt":
        return encrypted(item)
    else:
        return decrypted(item)
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
            
