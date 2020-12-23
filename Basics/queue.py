# a queue is a new type of data, a collection with different informations
# this structure is based on the FIFO principle (first in- first out) 
# a queue has 4 important operations

queue = []

# isEmpty()

def isEmpty():
    if len(queue) == 0:
        return True
    else:
        return False

#push

def push(val):
    queue.append(val)

#front
def front():
    return queue[0]

#pop

def pop():
    queue.reverse()
    queue.pop()
    queue.reverse()

push(2)
push(3)
push(4)
pop()
print(front())
print(isEmpty())
print(queue)