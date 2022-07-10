##print('dd')  exit()  divmod()  type()   id()

dkf='yuhang'                          ##print()
print(dkf[0:-2])
print("Test line 1", end="---")
print("Test line 2")

print("hello","world",sep="123")

print('dd\nkk')  #  \n换行
print(r'dd\nkk')  #  r: 取消

for i in range(1,5):  
    print("%-8d%-8d%-8d"%(i, i+1, i**(i+1)))  # display line by line, 8 spaces for each integer, leftward
###“d” in print(‘%d’%v) means the variable v is integer type; 
###“f” in print(‘%f’%v) means the variable v is a floating point number; 
###“s” in print(‘%s’%v) means the variable v is a string.

print('\n#########################\n')
x,y=divmod(17,5)                        ##divmod()
print(x,y)
print(str(divmod(17,5)))

x=123                                   ##type()
y=12.3
print(type(x),type(y))

t=1                                        ##id()
print(id(t))

print('\n#########################\n')

##int()  float()  str()  input()  eval()  help():   help(print)  bool()

                              
string='5+12'                               ##eval():dangerous
print(eval('2+3, 5'))
print(string, "=", eval(string))  

SDE="5+1"
print(SDE)
print(eval(SDE))

a=10
b=20
exp="a"+"*"+"b"
print("The result is:",eval(exp))

x = 0                                         ##bool()
print(bool(x))

print('\n#########################\n')  ##     zip()
print(list(zip([1,2,3,4], [[2,3,4],[2,3]])))
print(list(zip([1,2,3,4], (2,3,4,5,6,7))))

x = [1, 2, 3]              
y = [4, 5, 6]
print(list(zip(x, y)))

x2, y2 = zip(*zip(x, y))                       ##un-zip
print('x2 is', x2, 'and y2 is', y2)

print('\n################################\n') # filter()
##filter() returns a sequence for which the function returns True.
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

                                               ##### center()
for i in range (1,12,2): 
    print (('p'*i).center(11))

                                               ##  map()
######     ###       map(function_to_apply, list_of_inputs)
def square(x):
    return x**2
items = [1, 2, 3, 4, 5]
print(list(map(square, items)))

squared = list(map(lambda x: x**2, items))
print(squared)

print('\n#########################\n')           ##reduce()
##seq = [ s1, s2, s3, … , sn ], calling reduce(func, seq)
##[func(func(s1, s2),s3), … ,sn] 
from functools import reduce
def summation(x, y):
    return (x+y)
print(reduce(summation, [4, 1, 2, 3]))