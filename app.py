import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return "hello_world"

if __name__ == '__main__':
    uvicorn.run("app:app", port=1111, host='127.0.0.1')