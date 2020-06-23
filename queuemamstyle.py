from queue import Queue
q=Queue(maxsize=3)
q.put("king")
print(q)
print(q.pop())
print(q)   