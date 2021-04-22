import threading

class hello_world (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
        for x in range (4):
          print ("Hello World: "+ str(x))

hello_world().start()