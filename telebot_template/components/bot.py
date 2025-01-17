from telebot import TeleBot, types

from telebot_template.constants import BOT_TOKEN, ENV, WEBHOOK_URL
from telebot_template.components.services.messageService import get_last_message, create_message

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "This bot stores the messages you send to, except command messages. Use /last to see the last message you sent.")
    
@bot.message_handler(commands=["last"])
def last(message):
    last_message = get_last_message(message.chat.id, message.from_user.id)
    
    if last_message:
        bot.send_message(message.chat.id, f"Last message: {last_message.text}")
    else:
        bot.send_message(message.chat.id, "No messages have been sent yet.")
        
def filter_commands(message):
    return not (message.text.startswith("/start") or message.text.startswith("/last"))
      
@bot.message_handler(func=filter_commands)
def store_message(message):
    created_message = create_message(message.chat.id, message.from_user.id, message.text)
    
    if created_message:
        bot.send_message(message.chat.id, f"Message stored: {created_message.text}")
    else:
        bot.send_message(message.chat.id, "Could not store message.")

def run_bot():
    print("Starting bot...")
    
    bot.set_my_commands([
        types.BotCommand("start", "Get started."),
        types.BotCommand("last", "Get the last message you sent.")
    ])
    
    if ENV == "dev":
        print("Detected 'dev' environment, commencing polling...")
        
        bot.infinity_polling()
    else:
        print("Detected 'prod' environment, setting webhook...")
        
        if not WEBHOOK_URL:
            raise ValueError("WEBHOOK_URL is not set")
        
        bot.set_webhook(url=WEBHOOK_URL)
        