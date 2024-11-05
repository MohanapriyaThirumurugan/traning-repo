# Method Overriding (Inheritance-based Polymorphism)
# IF YOU SEE THE METHOD OVERRIDDING IN SAME FUNCTION BUT DIFFERENT
class tamil():
    def book(self):
        return "this is tamil book"
class English(tamil):
    def book(self):
        return "this is English book"
class Maths(tamil):
    def book(self):
        return "this is Maths book"
class Science(tamil):
    def book(self):
        return "this is science book"
# create object
bok=[English(),Maths()]

for i in bok :
    print(i.book())


class Bird:
    def fly(self):
        return "Flying in the sky"
class Airplane:
    def fly(self):
        return "Flying with engines"
# Duck typing example
def take_flight(flying_object):
    return flying_object.fly()
print(take_flight(Bird()))      
print(take_flight(Airplane()))  



# INHERITANCE IN PYTHON 

# THIS IS SINGLE INHERITANCE
# see, there is two differnt class and i am accese the frist class function ,i transferred frist class name as  a parameter in the second class a 
class fundamentals():
    def add(self):
        a=2
        b=3
        c=2+3
        print("add",c)
class funda(fundamentals):
    def sub(self):
        a=3
        b=2
        c=a-b
        print("sub",c)
exm=funda()
exm.sub()
exm.add()

#multiple inheritance
# i have three classes here and now i shared class name in third class as a parameter
# share one or more class in one class
class multipleinheritance():
    def mul(self):
        a=3
        b=3
        c=a*b
        print(c)
    def fact(self):
        a = 5
        result = 1
        for i in range(1, a + 1):
            result *= i
        print(result)
class mutiple2():
    def table(self):
     f = 5
     for i in range(1, 10 + 1):
        c = f * i
     print(c) 

    def hello(self):
        print("hello  preandsssss") 
class mul(multipleinheritance,mutiple2):
    def ff(self):
        print("...........hellooo") 
#object creation
val=mul()
val.fact()
val.table()
val.hello()
val.ff()

# multilevel intertance
class mul1():
    def h1(self):
        print("heloooooo everyone")
    def h2(self):
        print("print multilevel") 
class mul2(mul1,):
    def m1(self):
        print("m1 is there") 
    def m2(self):
        print("m2 has value") 
class mul3(mul2):
    def c1(self):
        print("helloooo c1") 
    def c2(self):
        print("hello c2")

mul=mul3()
mul.h1()
mul.c1()
mul.m2()
#herachy inheritance 
#one class inheritance to many class like the example

class dad():
    def money(self):
        print("hello dadaaaaaaaaaaaa")
class dad3(dad):
    def son1(self):
        pass
    def son2(self):
        pass
class dad1(dad):
    def son2(self):
        pass
    def son3(sel):
        pass
class dad2(dad):
    def son4(self):
        print("hello inheritance")
    def son5(self):
        pass
dd=dad2()
dd.son4()
dd.money()

#hybrid inheritance
# single and multiple and multilevel ,herachy inheritance called hybrid inheritance
class clg():
    def ece(self):
        print("ece is there")
    def cse(self):
        print("au cse")
class au(clg):
    def ece(self):
        print("au in ece")
    def cse(self):
        print("au in cse")
class clg2(au):
    def mech(self):
        pass
    def aero(self):
        pass
class clg3(clg2):
    def it(self):
        print("it is there")

gg=clg3()
gg.it()
# gg.ece()
gg1=au()
gg1.ece()
