from telebot_template.components.server import run_server
from threading import Thread, Event

shutdown_event = Event()
server_thread = Thread(target=run_server, daemon=True)

def main():
    server_thread.start()
    
    try:
        server_thread.join()
    except KeyboardInterrupt:
        print("Shutting down...")
        shutdown_event.set()
        server_thread.join()