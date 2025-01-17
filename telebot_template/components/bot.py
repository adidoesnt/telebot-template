from telebot import TeleBot

from telebot_template.constants import BOT_TOKEN, ENV, WEBHOOK_URL

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello!")

def run_bot():
    print("Starting bot...")
    
    if ENV == "dev":
        print("Detected 'dev' environment, commencing polling...")
        
        bot.infinity_polling()
    else:
        print("Detected 'prod' environment, setting webhook...")
        
        if not WEBHOOK_URL:
            raise ValueError("WEBHOOK_URL is not set")
        
        bot.set_webhook(url=WEBHOOK_URL)
        