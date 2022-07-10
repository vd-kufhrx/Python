import turtle
# import time
g_screen = None

def configScreen():
    s = turtle.Screen()
    s.tracer(50)
    
    s.setup()
    return s
def onScreenClick(x,y):
    t = turtle.Turtle("square")
    # t.shapesize(5,20,5)
    # t.color("red", "blue")
    g_screen.update()
    t.forward(50)
    g_screen.update()
   

def onKeyLeft():
    print('left')


g_screen = configScreen()
g_screen.onkey(onKeyLeft, "w")
g_screen._onscreenclick(onScreenClick)
g_screen.mainloop()