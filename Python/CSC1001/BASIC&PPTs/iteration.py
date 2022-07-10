def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)


def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        return 'done'

for n in fib_g(6):
    print(n)

###########################
print()

def f(x):
    if x == 0:
        return
    else:
        print(x)
        f(x-1)
f(3)
###############################3
print()

def f1(x):
    if x == 0:
        return
    else:
        f1(x-1)
        print(x)
f1(3)
#############################
print()

def fibiter(x):
    if x == 1:
        return 0
    elif x ==2:
        return 1
    return fibiter(x - 1) +fibiter(x - 2)
print(fibiter(4))
#################################################
print()

L = [1, 2, 3]
L2 = L.__iter__()
print(L2)

L = iter([1, 2, 3])
print(L.__next__())
print(L.__next__())
print(L.__next__())


for x in [1, 2, 3]:
    pass

iterator = iter([1, 2, 3])
while True:
    try:
        x = iterator.__next__()
        print(x, end=' ')
        
    except StopIteration as e:
        break


############????????
# class Sequence:
#     def __init__(self):
#         self.x = 0
#     def __next__(self):
#         self.x += 1
#         if self.x > 14:        #
#             raise StopIteration    #
#         return self.x**self.x
#     def __iter__(self):
#         return self
