####①
class A:
   def __new__(self):
       print("A's __new__() invoked")

   def __init__(self):
       print("A's __init__() invoked")

class B(A):
   def __new__(self):
       print("B's __new__() invoked")

   def __init__(self):
       print("B's __init__() invoked")

def main():
   b=B()
   a=A()

main()



####②
class C:
   def __new__(self):
       self.__init__(self)
       print("C's __new__() invoked")

   def __init__(self):
       print("C's __init__() invoked")

class D(C):
   def __new__(self):
       self.__init__(self)
       print("D's __new__() invoked")

   def __init__(self):
       print("D's __init__() invoked")

def main2():
   b=D()
   a=C()
main2()
##
##③
class E:
    def __new__(self):
        self.__init__(self)
        print("E's __new__() invoked")

    def __init__(self):
        print("E's __init__() invoked")

class F(E):
    def __init__(self):
        print("F's __init__() invoked")

def main3():
    b=F()
    a=E()
main3()



