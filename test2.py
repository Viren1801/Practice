from queue import Queue
NO_OF_THREADS = 4
queue_objects = [Queue() for i in range(NO_OF_THREADS)]

for i in queue_objects:
    print(i)


