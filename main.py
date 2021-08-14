from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

messages = {}


class Message(BaseModel):
    id: Optional[int]
    title: str
    body: str


class UpdateMessage(BaseModel):
    title: Optional[str]
    body: Optional[str]


@app.get("/")
def get_root():
    return {"status": True}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/messages")
def get_messages(search: Optional[str] = None):
    if search is None:
        return messages

    for message in messages:
        if messages[message].title == search:
            return messages[message]

    return {"error": "Not found"}


@app.get("/messages/{message_id}")
def get_message(*, message_id: int = Path(None, description="Message ID", gt=0, lt=99999999999)):
    try:
        return messages[message_id]
    except:
        return {"error": "Message does not exist"}


@app.post("/messages")
def create_message(message: Message):
    message_id = 1
    for item in messages.keys():
        message_id = item + 1

    message.id = message_id
    messages[message_id] = message

    return message


@app.put("/messages/{message_id}")
def update_message(message_id: int = Path(None, description="Message ID", gt=0, lt=99999999999), message: UpdateMessage = None):
    if message_id not in messages:
        return {"error": "Message does not exist"}

    if message.title != None:
        messages[message_id].title = message.title

    if message.body != None:
        messages[message_id].body = message.body

    return messages[message_id]


@app.delete("/messages/{message_id}")
def delete_message(message_id: int = Path(None, description="Message ID", gt=0, lt=99999999999)):
    if message_id not in messages:
        return {"error": "Message does not exist"}

    message = messages[message_id]

    del messages[message_id]

    return message
