import time
from threading import Thread

def myfunc(i):
    print( "Build wall")
    #time.sleep(1)
    #print( "finished sleeping from thread")

#for i in range(2):
while True:
    t1 = Thread(target=myfunc, args=(1,))
    t1.start()
    print("Thread 1")

    time.sleep(1)
    
    t2 = Thread(target=myfunc, args=(2,))
    t2.start()
    print("Thread 2")

    time.sleep(1)
    
    #t3 = Thread(target=myfunc, args=(2,))
    #t3.start()
    #print("Thread 3",i)
