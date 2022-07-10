class ListStack:
    
    def __init__(self):
        self.data = list()
    
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.__data.append(e)
    
    def top(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            return self.__data[self.__len__() - 1]

    def pop(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            return self.__data.pop()
hanoi = list()

def HanoiTower(n):

    global hanoi
    hanoi.append(('A', 'C', n))
    while len(hanoi):
        hanoi_top = hanoi[len(hanoi) - 1]
        hanoi = hanoi[0: len(hanoi) - 1]
        if hanoi_top[2] != 1:
            exchange = chr(198 - ord(hanoi_top[0]) - ord(hanoi_top[1]))
            hanoi.append((exchange, hanoi_top[1], hanoi_top[2] - 1))
            hanoi.append((hanoi_top[0], hanoi_top[1], 1))
            hanoi.append((hanoi_top[0], exchange, hanoi_top[2] - 1))
        else:
            print(hanoi_top[0], '-->', hanoi_top[1])
            
HanoiTower(3)





class ListStack:
    
    def __init__(self):
        self.data = list()
    
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.__data.append(e)
    
    def top(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            return self.__data[self.__len__() - 1]

    def pop(self):
        if self.is_empty():
            print('The stack is empty.')
        else:
            a = self.__data[self.__len__() - 1]
            self.__data = self.__data[0: self.__len__() - 1]
            return a

def HanoiTower(n):
    stack = ListStack()
    stack.data.push(('A', 'C', n))
    while len(stack):
        stack_top = stack.data.top()
        stack.data.pop()
        if stack_top[2] != 1:
            exchange = chr(198 - ord(stack_top[0]) - ord(stack_top[1]))
            stack.push((exchange, stack_top[1], stack_top[2] - 1))
            stack.push((stack_top[0], stack_top[1], 1))
            stack.push((stack_top[0], exchange, stack_top[2] - 1))
        else:
            print(stack_top[0], '-->', stack_top[1])
            

try:
    n = int(input("Value:"))
except:
    print('Please input a positive integer')
HanoiTower(3)