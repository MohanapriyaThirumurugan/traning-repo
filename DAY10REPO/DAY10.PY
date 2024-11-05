# ENCABSULATION
# ENCAPSULATION FOR PRIVATE AND PROTECTED THE CLASS


#private class
class company():
    def __init__(self):
        self.__companyname="google"
    def companyy(self):
       print(self.__companyname) 
c1=company()
c1.companyy()
# print(c1.__companyname)-------> thiis is not wok because it protect if you want to get the acces means only way is function


#protected class
class company1():
    def __init__(self):
        self._companyname="microsoft"
    def companey(self):
        print(self._companyname)
d1=company1()
d1.companey()

#  abstraction in python
# abstraction is used for hiding the unwanted things
from abc import ABC ,abstractmethod
class car(ABC):
    @abstractmethod
    def moveforward(self):
        pass
    @abstractmethod
    def movebackward(self):
        pass
    @abstractmethod
    def fm(self):
        pass
class  swift(car):
    def moveforward(self):
        print("swfit car moveforwar")
    def movebackward(self):
        print("swfit car movebackward")
    def fm(self):
        print("swfit car fm")

class  tata(car):
    def moveforward(self):
        print("tata car moveforwar")
    def movebackward(self):
        a=6
        b=6
        c=a+b
        print("tata car movebackward",c)
    def fm(self):
        print("tata car fm")
class honda(car):
     def moveforward(self):
        print("honda car moveforwar")
     def movebackward(self):
        print("thonda car movebackward")
     def fm(self):
        print("honada car fm")
# creating a object
h1=tata()
h1.movebackward()
c1=honda()
c1.moveforward()
