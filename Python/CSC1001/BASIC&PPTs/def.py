def substract(
    a,
    b):
    return (a-b)
print(substract(5,3))
print(substract(b=5,a=3))

print('\n#######################\n')

def print_info1(name, age=35):###default
    print("Name:",name)  
    print("Age:",age)
print_info1(name="Alice")

print('\n#######################\n')

def printinfo2(*vartuple):        ###  *   
    
    for var in vartuple:
        print(var)        # return = return None
    return              ####return : exit the function 
printinfo2(10,20,30)  ##these numbers will be stored in a tuple


print('\n#######################\n')


###  **   : dictionary          #  **
def printdict(**kaj):
    print(kaj)
    return
printdict(john=10, jill= 12, david= 15)


print('\n#######################\n')



#global:
x = 50
def func():
    global x 
    x=2
print(x)
func()
print(x)


print('\n#######################\n')

def foo():
    a=1 
    b=2
    return a,b      ## return: packed up in a tuple
print(foo())


print('\n#######################\n')

##Find the greatest common divisor gcd
def gcd(a,b):
    low = min(a,b)
    high = max(a,b)

    if low == 0:
        return high
    elif low == 1:
        return 1 
    else:
        return gcd(low,high%low)

print(gcd(12,13))
print(gcd(13,26))
print(gcd(444,111))

print('\n#######################\n')

##lambda
fn = lambda x : x**2
print(fn(9))


print((lambda x: x**2)(3))

print((lambda x: x if x > 5 else 3)(6))

print((lambda x: [i*x for i in range(5)])(4))


print('\n#######################\n')

g = (x ** x for x in range(5))
for n in g:
    print(n)

print('\n#######################\n')

n = (e for e in range(50000000) if not e % 3)
i = 0
for e in n:
    print(e)
    i += 1
    if i > 5:
        break

####################
print('\n#########################\n')

list_with_list = [[1, 2, 3, 4, 5], \
    [6, 7, 8, 9, 10], [11, 12, 13, 14,15]]
for (head, *body, tail) in list_with_list:
    print(head, tail)

print('\n#######################\n')


print('\n#######################\n')