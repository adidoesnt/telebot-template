from telebot_template.components.server import run_server
from telebot_template.components.bot import run_bot
from threading import Thread, Event

shutdown_event = Event()

bot_thread = Thread(target=run_bot, daemon=True)
server_thread = Thread(target=run_server, daemon=True)

def main():
    bot_thread.start()
    server_thread.start()
    
    try:
        bot_thread.join()
        server_thread.join()
    except KeyboardInterrupt:
        print("Shutting down...")
        shutdown_event.set()
        