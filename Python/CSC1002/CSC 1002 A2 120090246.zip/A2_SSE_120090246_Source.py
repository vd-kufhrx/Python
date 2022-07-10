from turtle import Turtle, Screen
import random

### Part 1                Before Motion
# Initial state of the board and the snake
game_state = 0
start = 0
pause = 9
run = 1
win = 2
lose = -1
total_time = 0
contact = 0
food_left = 0
move = 'PAUSE'
original_move = 'PAUSE'
 
# Generate a screen from turtle
def generate_screen():
    global screen
    screen = Screen()
    screen.setup(width = 662, height = 744, starty = 20)
    screen.tracer(False)
    screen.title('SnakeGame---Yuhang')

# Generate the boundary of the game
def generate_region():
    segments = Turtle()
    segments.hideturtle()
    segments.up()
    segments.goto(-251, 209)
    segments.down()
    segments.goto(-251, -292)
    segments.goto(251, -292)
    segments.goto(251, 210)
    segments.goto(-251, 210)
    segments.goto(-251, 211)
    segments.goto(251, 211)
    segments.goto(251, 292)
    segments.goto(-251, 292)
    segments.goto(-251, 211)

# Set words on the top of the screen
def generate_countings():
    global countings
    countings = generate_turtle(pos = (-230, 240))
    countings.write('Contact: {}              Time: {}              Motion: {}'.format(contact, total_time, 'PAUSE'), \
              font = ('Arial', 14, 'normal'))

# Set the welcome text in move area
def welcome_text():
    global text
    text = generate_turtle(pos = (0, -50))
    text.write('Welcome to Yuhang\'s version of snake...\n\n' 
                'You are going to use the 4 arrow keys to move the snake\n' 
                'around the screen, trying to sonsume all the food items\n'
                'before the moster catches you...\n\n'
                'Click anywhere on the screen to start the game, have fun!!', \
                align = 'center', font = ('Arial', 12, 'normal'))


# Set all turtle objects
def generate_turtle(show = False, color = 'black', pos = (0, -41)):
    turtle = Turtle('square')
    turtle.color(color, color)
    turtle.up()
    turtle.setpos(pos)
    if not show:
        turtle.hideturtle()
    return turtle


###    Part 2                  After click  

# The function of the four directions
def GO_UP():
    global snake, move
    snake[0].setheading(90)
    move = 'UP'

def GO_DOWN():
    global snake, move
    snake[0].setheading(270)
    move = 'DOWN'

def GO_LEFT():
    global snake, move
    snake[0].setheading(180)
    move = 'LEFT'

def GO_RIGHT():
    global snake, move
    snake[0].setheading(0)
    move = 'RIGHT'

# Mapping functional keys
def PRESS_KEY():
    global screen
    screen.onclick(start_Game)
    screen.onkey(PAUSE, "space")
    screen.onkey(GO_RIGHT, "Right")    
    screen.onkey(GO_LEFT, "Left")
    screen.onkey(GO_UP, "Up") 
    screen.onkey(GO_DOWN, "Down")

# Set the information of the nums_to_eat
def set_food():
    global nums_to_eat, food_turtles
    nums_to_eat = []
    num_used = []
    food_turtles = []
    while len(nums_to_eat) < 9:
        food_x = random.randrange(-200, 200, step = 20)
        food_y = random.randrange(-241, 159, step = 20)
        if(food_x, food_y) not in num_used:
            num_used.append((food_x, food_y))
            food_turtle = generate_turtle(show = False, pos = (food_x, food_y - 10))
            food_turtles.append(food_turtle)
            food_number = len(food_turtles)
            nums_to_eat.append({'number' : food_number, 'pos' : (food_x, food_y), 'state' : 1})
            food_turtle.write(str(food_number), align = 'center', font = ('Arial', 12, 'normal'))
    
    nums_to_eat.append({"number": 5, "pos": (0, -41), "state": 1})
    food_turtle = generate_turtle(show = False)
    food_turtles.append(food_turtle)
    screen.update()

# Get the position of the turtle object called
def get_pos_xy(turtle):
    y = round(turtle.ycor())
    x = round(turtle.xcor())
    return(x, y)

# Check whether the numbers are all eaten
def food_remain():
    global nums_to_eat
    for food in nums_to_eat:
        if food['state'] == 1:
            return True
    return False

# Realize the function of eating food
def eat_food(number, pos):
    global food_left, nums_to_eat
    food_left += number
    for i in range(len(food_turtles)):
        if nums_to_eat[i]['pos'] == pos:
            nums_to_eat[i]['state'] = 0
            food_turtles[i].clear()

# Get the time used, updating per second.
def set_timer():
    global contact, total_time, game_state
    total_time += 1
    screen.ontimer(set_timer, t = 1000)

# Set the udpate time of the screen
def screen_update():
    global game_state
    if game_state == run:
        screen.update()
    screen.ontimer(screen_update, t = 100)

# The parameter of the snake
def A_snake():
    global snake
    snake = []
    head = generate_turtle(show = True, color = 'red', pos = (0, -41))
    snake.append(head)\

# The parameter of the monster
def A_monster():
    global monster
    monster_xy = [(-140, -141), (140, -141), (-140, 139), (140, 139)]
    monster = generate_turtle(show = True, color = 'purple', pos = monster_xy[random.randint(0, 3)])

# The function of moving the snake
def snake_move():
    global game_state, contact, food_left, snake, nums_to_eat, snake
    if original_move:
        countings.clear()
        t = 200
        if game_state == run:
            head = snake[0].clone()
            pos_head = get_pos_xy(head)
            x = pos_head[0]
            y = pos_head[1]
            
            pos_food = [food['pos'] for food in nums_to_eat]
            if pos_head in pos_food:
                food = pos_food.index(pos_head)
                if nums_to_eat[food]['state'] == 1:
                    eat_food(nums_to_eat[food]['number'], nums_to_eat[food]['pos'])
            if (-250 >= (x - 20) and head.heading() == 180) or \
            ((x + 20) >= 250 and head.heading() == 0) or \
            (-291 >= (y -20) and head.heading() == 270) or \
            ((y + 20) >= 209 and head.heading() == 90):
                head.hideturtle()
                countings.write('Contact: {}               Time: {}               Motion: {}'.format(contact, total_time, 'PAUSE'), \
                          font = ('Arial', 14, 'normal'))
            else:
                head.forward(20)
                snake.insert(0, head)
                snake[1].color('blue', 'black')
                snake[-1].hideturtle()
                if food_left != 0:
                    food_left -= 1
                    t = 400
                else:
                    snake.pop()
                if not food_remain():
                    game_state = win
                    end_Game()
                countings.write('Contact: {}               Time: {}               Motion: {}'.format(contact, total_time, move), \
                          font = ('Arial', 14, 'normal'))
        else:
            countings.write('Contact: {}               Time: {}               Motion: {}'.format(contact, total_time, 'PAUSE'), \
                      font = ('Arial', 14, 'normal'))
        screen.ontimer(snake_move, t = t)

# The function of moving the monster
def monster_move():
    global contact, game_state, total_time, monster
    differ_x = monster.xcor() - snake[0].xcor()
    differ_y = monster.ycor() - snake[0].ycor()

    if game_state == run:
        if abs(differ_x) > abs(differ_y):
            if differ_x > 0:
                monster.setheading(180)
            elif differ_x < 0:
                monster.setheading(0)
        else:
            if differ_y > 0:
                monster.setheading(270)
            elif differ_y < 0:
                monster.setheading(90)
        monster.forward(20)

    for i in range(len(snake)):
        if game_state == run and get_pos_xy(snake[i]) == get_pos_xy(monster):
            if i == 0:
                game_state = lose
                end_Game()
            else:
                if game_state != pause and game_state != win and game_state != lose:
                    contact += 1
    t = random.randint(400, 500)
    screen.ontimer(monster_move, t = t)


###   Part 3        State of the game: start, pause, end
# Start the game
def start_Game(x, y):
    global game_state, text, move
    if game_state == start:
        text.clear()
        set_food()
        game_state = run
        move_list = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        move = move_list[random.randint(0, 3)]

# Pause the game
def PAUSE():
    global game_state, move, original_move
    if game_state == run:
        game_state = pause
        original_move = move
        move = 'PAUSE'
    elif game_state == pause:
        game_state = run
        move = original_move

# End of the game
def end_Game():
    global game_state, move, original_move
    game_result = generate_turtle(pos = (0, -41))
    if game_state == win:
        game_result.pencolor('red')
        game_result.write('Winner!!', align = 'center', font = ('Arial', 12, 'normal'))
    elif game_state == lose:
        game_result.pencolor('purple')
        game_result.write('Game over!!', align = 'center', font = ('Arial', 12, 'normal'))
    move = 'PAUSE'
    original_move = ''
    countings.write('Contact: {}               Time: {}               Motion: {}'.format(contact, total_time, move), \
              font = ('Arial', 14, 'normal'))

# Call all the functions to start the game
if __name__ == '__main__':
    generate_screen()
    generate_region()
    generate_countings()
    welcome_text()
    screen.update()
    A_monster()
    A_snake()
    screen.listen()
    PRESS_KEY()
    snake_move()
    monster_move()
    set_timer()
    screen_update()
    screen.mainloop()