from queue import Queue

#push, pop
q = Queue()

q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())

q.qsize()
