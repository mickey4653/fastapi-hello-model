from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Foundations API", version="1.0")

# Define a data model for POST requests
class Message(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to your first AI API 🚀"}

@app.post("/echo")
def echo_message(msg: Message):
    return {"your_message": msg.text}
