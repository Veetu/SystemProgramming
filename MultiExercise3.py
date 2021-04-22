import threading

num = 1

def main():
    
    for i in range(7):
        thread = threading.Thread(target=hello_world)
        thread.start()

        thread.join()

def hello_world():

    print("Inside hello_world()")

    global num
    L = threading.Lock()
    L.acquire()

    print("Hello world: " + str(num))
    num += 1

    L.release()

main()
