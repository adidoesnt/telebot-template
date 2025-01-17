from peewee import Model
from telebot_template.components.database import db

class BaseModel(Model):
    class Meta:
        database = db