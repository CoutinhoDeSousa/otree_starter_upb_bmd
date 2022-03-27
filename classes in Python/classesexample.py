class MyClass:
    x = 5
    str = "This is a test string"

    def print_function(self):
        print((self.str+" ")*self.x)


myc = MyClass()

myc.print_function()
# manipulate x
myc.x = 2
# manipulate str
myc.str = "laola"
# print again to see the difference
myc.print_function()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def hello(self):
        # formatting the string name and integer age into the string to print
        print("Hello my name is %s and i'm %i old" % (self.name,self.age))

    def hello2(self):
        # concatenating the string to print , therefor you have to cast the age variable to string with str()
        print("Hello my name is " + self.name + " and i'm " + str(self.age) + " old")


person1 = Person("Karl", 22)
Person.hello(person1)
person1.hello()
person1.hello2()



class InnerClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.v = x+y+z

    def print_all(self):
        print("x: %i" % self.x)
        print("y: %i" % self.y)
        print("z: %i" % self.z)
        print("v: %i" % self.v)


class OuterClass:

    def __init__(self, inner):
        self.x = inner.x-inner.y
        self.y = 27
        self.z = inner.z**2
        self.v = -1
        self.inner = inner

    def print_all(self):
        print("x: %i" % self.x)
        print("y: %i" % self.y)
        print("z: %i" % self.z)
        print("v: %i" % self.v)

    def print_everything(self):
        print("Inner Variables")
        self.inner.print_all()
        print("Outer Variables")
        self.print_all()


inn = InnerClass(1, 2, 3)
out = OuterClass(inn)

out.print_everything()



class BeautyContestPlayer:
    def __init__(self,guessnumber,isWinner):
        self.guessnumber=guessnumber
        self.isWinner = isWinner
    def printmyAttributes(self):
        print("The number I typed is",self.guessnumber)
        print ("Did I win",self.isWinner)

Fabian = BeautyContestPlayer(50.0,True)
Fabian.printmyAttributes()