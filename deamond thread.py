import threading
import time

def background_task():
    while True:
        print("Deamond thread is running....")
        time.sleep(2)

deamon_thread = threading.Thread(target=background_task, args=(), daemon=True)
deamon_thread.start()

print("Zacni program")
time.sleep(11)
print("Ukonci program")

