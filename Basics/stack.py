#a stack is a new type of data, a collection of dates which is ordered and which have a top
#a stack is based on the LIFO principle (last in -first out)
#a stack has 4 important operations

stack = []

#isEmpty()

def isEmpty() :
    if  len(stack) == 0:
        return True
    else:
        return False

#push()

def push(value):
    stack.append(value)

#front()

def front():
    return stack.pop()

#pop()

def pop():
    stack.pop()

push(2)
push(3)
push(5)
pop()
print(isEmpty())
print(front())
