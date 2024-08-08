import threading
import time
 
class messanger(threading.Thread):
    def run(self):
       for _ in range(10):
           print(threading.current_thread().getName())
           time.sleep(5)
x=messanger(name="message is send")
y=messanger(name="message is receive")
x.start()
y.start()
 