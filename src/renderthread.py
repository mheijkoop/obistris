from threading import Thread
from time import sleep, time

class RenderThread(Thread):
    
    def __init__(self, callback):
        self.callback = callback
        super(__class__, self).__init__(name="RenderThread", daemon=True)
    
    def run(self):
        prev_time = time()
        while True:
            self.callback()
            print((1/(time()-prev_time)), "fps")
            prev_time = time()