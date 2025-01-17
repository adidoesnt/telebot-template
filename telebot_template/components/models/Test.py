from telebot_template.components.models.BaseModel import BaseModel
from peewee import AutoField, TextField

class Test(BaseModel):
    id = AutoField()
    data = TextField()
    