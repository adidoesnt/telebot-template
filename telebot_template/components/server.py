from fastapi import FastAPI
import uvicorn
from telebot_template.constants import HOST, PORT
from telebot_template.components.database import check_db_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

def run_server():
    check_db_connection()
    uvicorn.run(app, host=HOST, port=PORT)
    