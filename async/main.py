import threading

def myTask():
    print("Hello world: {}".format(threading.current_thread()))

myThread = threading.Thread(target=myTask())
myThread.start()