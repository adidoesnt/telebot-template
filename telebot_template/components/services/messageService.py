from telebot_template.components.models.Message import Message
from peewee import DoesNotExist

def create_message(chat_id, from_id, text):
    try:
        print(f"Creating message for chat_id: {chat_id}, from_id: {from_id}, text: {text}")
        
        message = Message.create(
            chat_id=chat_id,
            from_id=from_id,
            text=text
        )
        
        print(f"Message created: {message.text}")
        
        return message
    except:
        print("Error: Could not create message")
        return None

def get_last_message(chat_id, from_id):
    try:
        print(f"Getting last message for chat_id: {chat_id}, from_id: {from_id}")
        
        messages = Message.select().where(
            Message.chat_id == chat_id,
            Message.from_id == from_id
        ).order_by(
            Message.id.desc()
        ).get()
        
        message = Message.select().where(
            Message.chat_id == chat_id,
            Message.from_id == from_id
        ).order_by(
            Message.id.desc()
        ).first()
        
        print(f"Last message: {message.text}")
        
        return message
    except DoesNotExist:
        print("Error: Could not get last message")
        
        return None