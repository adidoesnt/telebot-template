from telebot_template.components.models.BaseModel import BaseModel
from peewee import AutoField, IntegerField, TextField

class Message(BaseModel):
    id = AutoField()
    chat_id = IntegerField()
    from_id = IntegerField()
    text = TextField()
    