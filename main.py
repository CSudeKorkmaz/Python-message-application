from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Message(BaseModel):
    id: int
    text: str


messages = []


@app.post("/messages", response_model=Message)
def create_message(message: Message):
    messages.append(message)
    return message


@app.get("/messages", response_model=List[Message])
def get_messages():
    return messages


@app.get("/messages/{message_id}", response_model=Message)
def get_message(message_id: int):
    for message in messages:
        if message.id == message_id:
            return message
        raise HTTPException(status_code=404, detail="Message not found")
