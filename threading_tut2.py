import threading
import time

class messenger(threading.Thread):
    def run(self):
      for _ in range(10):
         print(threading.current_thread().getName())
         time.sleep(1)

x=messenger(name="sent message")
y=messenger(name="recevice message")
x.start()
y.start()