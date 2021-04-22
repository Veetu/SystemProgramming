import threading

def hello_world():
    for x in range (4):
        print ("Hello World: "+ str(x))

if __name__ == "__main__":
   
    x = threading.Thread(target=hello_world)
    x.start()