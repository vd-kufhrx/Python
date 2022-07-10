import random  # random


def generate_a_list(n_line): # int, meaning n_line rows n_line columns puzzle
    numbers = list()  # generate a list
    
    for i in range(1, n_line ** 2):
        numbers.append(i)
    numbers.append(' ')
    numbersInOrder = numbers.copy()
    return numbers, numbersInOrder


def printPuzzle(  # turn the list into a n * n form and print it.
    _n_line,    # int, meaning n_line rows n_line columns puzzle
    _numbers):  # A list to be printed.
    count = 0
    
    for i in _numbers:
        i_in_str = str(i)
        i_formatted = i_in_str.ljust(2)
        count += 1
        if count == _n_line:
            count = 0
        print(i_formatted, end='\n' if count == 0 else '  ')
    return


def countInverseNumber(    
    _n_line,   # int, meaning n_line rows n_line columns puzzle
    _numbers): # A list to be printed.
  
    inverseNumber = 0  # count the inverse number
    for formerNumber in _numbers[:_n_line ** 2 - 1]:
        place = _numbers.index(formerNumber)
        for lattterNumber in _numbers[place + 1:]:
            try:
                if formerNumber > lattterNumber:
                   inverseNumber += 1
            except: None
    return inverseNumber


def generate_solvable_puzzle(_n_line):    # generate a solvale puzzle list
    numbers, numbersInOrder = generate_a_list(_n_line)
    while True:  
        random.shuffle(numbers)      
        inverseNumber = countInverseNumber(_n_line,numbers)
        p = numbers.index(' ')
        distance = p - _n_line ** 2 + 1  # distance from initial empty space
        if _n_line % 2 == 1 and inverseNumber % 2 == 0:
            break
        elif _n_line % 2 == 0:
            if inverseNumber % 2 == 0 and distance % 2 == 0:
                break
            elif inverseNumber % 2 == 1 and distance % 2 == 1:
                break
    return numbers, numbersInOrder


def get_dimension():
    print('Welcome to my sliding puzzle game')    #describe thhe game.
    print('The puzzle get solved when numbers arranged from the smallest to the largest.')
    
    while True:  # input your desired lines
        try:
            n_line = int(input('Enter your desired dimension from 3 to 10:'))
            if 2 < n_line < 11:
                break
            else:
                print('Invalid input, Please try it again.')
        except:
            print('Invalid input, Please try it again.')
    return n_line


def get_four_direction_lettters():
    
    while True:    
        left = input('Enter a symbol meaning sliding a number to the left:')
        right = input('Enter a symbol meaning sliding a number to the right:')
        up = input('Enter a symbol meaning sliding a number to the up:')
        down = input('Enter a symbol meaning sliding a number to the down:')
        
        direction_list = list()
        direction_list.append(down)
        direction_list.append(up)
        direction_list.append(right)
        direction_list.append(left)
        
        if len(direction_list) == len(set(direction_list)):  
            break         #to ensure that the four directon keys are differennt to each other.
        else:
            print('Please input four different letters for directions.')
    return left, right, up, down


def move(
    _left,     # direction1: to the left 
    _right,    # direction2: to the right 
    _up,       # direction3: to thhe up
    _down,     # direction4: to the down
    _n_line,   # int, meaning n_line rows n_line columns puzzle
    _numbers): # A list to be printed.
    
    while True: 
        p = _numbers.index(' ')   
               #p : int,  character index of ' ' in numbers_input list
        if p == 0:           #get the input direction
            command = input('Enter direction:(left:' + _left + \
                '  up:' + _up + ')')
            if command == _left or command == _up: break
            else: print('Please input the right command.')
        elif p == _n_line ** 2 - 1:
            command = input('Enter direction:(right:' + _right + \
                '  down:' + _down + ')')
            if command == _right or command == _down: break
            else: print('Please input the right comsmand.')
        elif p == _n_line - 1:
            command = input('Enter direction:(right:' + _right + \
                '  up:' + _up + ')')
            if command == _right or command == _up: break
            else: print('Please input the right command.')
        elif p == _n_line * (_n_line - 1):
            command = input('Enter direction:(left:' + _left + \
                '  down:' + _down + ')')
            if command == _left or command == _down: break
            else: print('Please input the right command.')
        elif 1 <= p <= _n_line - 1:
            command = input('Enter direction:(right:' + _right + \
                '  up:' + _up + '  left:' + _left + ')')
            if command == _up or command == _right or \
                command == _left: break
            else: print('Please input the right command.')
        elif 1 + _n_line * (_n_line - 1) <= p <= _n_line ** 2 - 2:
            command = input('Enter direction:(right:' + _right + \
                '  down:' + _down + '  left:' + _left + ')')
            if command == _right or command == _down or \
                command == _left: break
            else: print('Please input the right command.')
        elif p % _n_line == 0:
            command = input('Enter direction:(up:' + _up + \
                '  down:' + _down + '  left:' + _left + ')')
            if command == _up or command == _down or \
                command == _left: break
            else: print('Please input the right command.')
        elif p % _n_line == _n_line - 1:
            command = input('Enter direction:(right:' + _right + \
                '  down:' + _down + '  up:' + _up + ')')
            if command == _right or command == _down or \
                command == _up: break
            else: print('Please input the right command.')
        else:
            command = input('Enter direction:(right:' + _right + \
                '  down:' + _down + '  up:' + _up + '  left:' + _left + ')')
            if command == _right or command == _down or \
                command == _up or command == _left: break
            else: print('Please input the right command.')
            
    if command == _up:    # element in the list changing formula of the move 
        _numbers[p], _numbers[p + _n_line] = _numbers[p + _n_line], _numbers[p]
    elif command == _down:
        _numbers[p], _numbers[p - _n_line] = _numbers[p - _n_line], _numbers[p]
    elif command == _left:
        _numbers[p], _numbers[p + 1] = _numbers[p + 1], _numbers[p]
    elif command == _right:
        _numbers[p], _numbers[p - 1] = _numbers[p - 1], _numbers[p]
        

def run():    
    times = 0     #steps you have operated
    n_line = get_dimension()
    left, right, up, down = get_four_direction_lettters()
       
    while True:   #ensure the randomized puzzle won't get solved in less than 1 step.
        numbers, numbersInOrder = generate_solvable_puzzle(n_line)
        if numbersInOrder != numbers:
            break 
    
    while True: 
        printPuzzle(n_line,numbers)
        print()
        move(left,right,up,down,n_line,numbers)
        print(); print()
        if numbersInOrder == numbers:
            printPuzzle(n_line,numbers)
            print('Congratulations, you have finished it!')
            print('total steps:', times)
            break 
        times += 1   
        

def main():
    run()
    gamerestart = input("Do you want to play again?Input y for yes, other to exit.")
    if gamerestart in ["Y","y"]:
        main()


if __name__ == '__main__':
    main()