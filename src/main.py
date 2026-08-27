import os
from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str     # expect JSON body {"prompt": "..."}

class ChatResponse(BaseModel):
    prompt: str     # return JSON body {"response": "..."}

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response_text = "..."
    return ChatResponse(response=response_text)

def main():
    print("Hello from gotta-go-fastapi!")


if __name__ == "__main__":
    main()
