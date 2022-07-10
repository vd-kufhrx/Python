import turtle 
import time 










def onScreenClick(x,y):
    global g_snake
    g_snake = turtle.Turtle("square")
    g_screen.update()
    g_screen.ontimer(onTimer, 500)

def onKeyPressed():
    print('A key pressed.')

def onTimer():
    print('On timer call')
    g_snake.forward(100)
    g_screen.update() 







def configurePlayerArea():
    s = g_screen  ###############
    # intro = createTurtle(10, 10, 'yellow')
    # intro.hideturtle()
    # intro.goto(-100, s.ycor())
    status = createTurtle(0, 0, 'yellow')
    status.hideturtle()
    # status.goto(-200, s.ycor())

    return status

def configScreen():
    s = turtle.Screen()
    s.tracer(0)  #disable auto screen refresh
    s.title("Snake Game by Yuhang")
    s.setup(500+50*2, 500+50*2+100)
    s.mode("standard")
    return s

def createTurtle(x, y, color = 'red', border = 'black'):
    t = turtle.Turtle("square")
    t.color(border, color)
    t.up()
    t.goto(x,y)
    return t

def onArrowKeyPressed(key):
    global g_keypressed
    g_keypressed = key
    setSnakeHeading(key)
    updateStatus()

def updateStatus():
    g_status.clear()
    g_status.write(g_keypassword, font = ('arial', 15, 'bold'))
    g_screen.update()

def setSnakeHeading(key):
    if key in HEADING_BY_KEY.keys():
        g_snake.setheading( HEADING_BY_KEY[key] )

def onTimeSnake():
    print('onTimeSnake')

    if g_keypressed == None:
        g_screen.ontimer(onTimeSnake, 200)
        return

    #clone the head as body
    g_snake.color(*COLOR_BODY)
    g_snake.stamp()
    g_snake.color(COLOR_HEAD)

    # Advance snake
    g_snakeforward(20)

    #shifting or extending the tail.
    # Remove the last square on shifting.
    if len(g_snake.stampItems) > g_snake_sz:
        g_snake.clearstamps(1)

    g_screen.update()
    g_screen.ontimer(onTimeSnake, 200)

    g_screen.update()

    g_screen.ontimer(onTimeSnake, 200)


def onTimeMonster():
    print('onTimeMonster')
    dir = list(range(0, 306, 90))
    random.shuffle(dir)
    g_monster.setheading(dir[0])
    g_monster.forward(20)

    g_screen.update()
    g_screen.ontimer(onTimeMonster, 600)


def startgame(x,y):
    g_screen.onscreenclick(None)
    g_intro.clear()

    g_screen.onkey(partial(onArrowKeyPressed, KEY_UP), KEY_UP)
    g_screen.onkey(partial(onArrowKeyPressed, KEY_DOWN), KEY_DOWN)
    g_screen.onkey(partial(onArrowKeyPressed, KEY_LEFT), KEY_LEFT)
    g_screen.onkey(partial(onArrowKeyPressed, KEY_RIGHT), KEY_RIGHT)

    g_screen.ontimer(onTimeSnake, 500)
    g_screen.ontimer(onTimeMonster, 1000)

if __name__ == "__main__":
    g_screen = configScreen()
    g_status = configurePlayerArea()

    updateStatus()

    g_monster =  createTurtle(-110, -110, 'purple', 'black')
    g_snake = createTurtle(0, 0, "red", "black")  

    g_screen.onscreenclick(startgame)      

