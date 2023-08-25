from time import sleep
from random import random
from threading import Thread
from queue import Queue
n1 = int(input("first"))
n2 = int(input("second"))

# producer task
def producer(queue):
    print('Producer: Running')
    # generate items
    for i in range(n1):
        # generate a value
        value = i*i
        # block, to simulate effort
        sleep(1)
        # create a tuple
        item = (i, value)
        # add to the queue
        queue.put(item)
        # report progress
        print(f'>producer added {item}')
    # signal that there are no further items
    queue.put(None)
    print('Producer: Done')


# consumer task
def consumer(queue):
    print('Consumer: Running')
    # consume items
    for j in range(n2):
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        # block, to simulate effort
        sleep(1)
        # report
        print(f'>consumer got {item}')
    # all done
    print('Consumer: Done')


# create the shared queue
queue = Queue()
# start the consumer
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
# start the producer
producer = Thread(target=producer, args=(queue,))
producer.start()
# wait for all threads to finish
producer.join()
consumer.join()