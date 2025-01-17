from fastapi import FastAPI
import uvicorn
from telebot_template.constants import HOST, PORT

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

def run_server():
    uvicorn.run(app, host=HOST, port=PORT)
    