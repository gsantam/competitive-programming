import time
import inspect
import queue
import threading

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()
    
class NumberedThread():
    def __init__(self):
        self.atomic_variable = 9

    def try_print(self,n):
        while True:
            if self.atomic_variable==n:
                print(n)
                self.atomic_variable-=1
                break
n = 10
numberedThread = NumberedThread()
for i in range(n):
    thread = Thread(numberedThread.try_print,i)