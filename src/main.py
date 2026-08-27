import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}
    
def main():
    print("Hello from gotta-go-fastapi!")


if __name__ == "__main__":
    main()
