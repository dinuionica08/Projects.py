# a lambda function is an anonimous function with more arguments, but with an only one expression

x = lambda x2 : x2 + 10
print(x(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(2))

def triple(n) :
    return lambda a : a * a * n
t = triple(2)
print(t(2))