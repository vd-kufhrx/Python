from math import pi

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
        
    def getPerimeter(self):
        return 2 * self.radius * pi 

    def getArea(self):
        return self.radius * self.radius * pi

    def setRadius(self, radius):
        self.radius = radius

def printArea(c, times):
    while times >= 1:
        c.radius = c.radius + 1
        times = times - 1
        print(times, c.radius, c.getArea())

def main():
    myCircle = Circle()
    n = 5
    printArea(myCircle, n)
    print(myCircle.radius)
    print(n)

main()
