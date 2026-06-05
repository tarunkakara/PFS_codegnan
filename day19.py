'''
---------------------------Day 19 of Python Class----------------------------
Inheritance:
--> This allows one class to aquire the properties and methods of another class.
Types:
---------------------------------------------------------------------------------------------------
1.Single Inheritance:
--> A class Inherts from a single parent class.
EX:
class father:
    def land(self):
        print("I am father have 5A")
class tarun(father):
    def my_own(self):
        print("I have my land 2A")

fam = tarun()

fam.land()

---------------------------------------------------------
2.Multiple Inheritance:


--> parent1      parent2
       |-----|-----|
           Child
           
-->A class Inherts from a Multiple  parent class.
EX:
class father:
    def Land(self):
        print("I have 5A land")

class mother:
    def Gold(self):
        print("I have 5 kg Gold")


class son(father,mother):
    def mine(self):
        print("I have Car")

aow = son()

aow.Land()
aow.Gold()

---------------------------------------------------------------------------------------------------

3.Multi-Level Inheritance:

Grandfather
    |
 father
    |
  son



--> A class Inherits from a parent class and another class inherit from that child class
EX:
class grandfather:
    def land(self):
        print("I have 5A of land")

class father(grandfather):
    def flat(self):
        print("I have flat in HYD")

class son(father):
    def car(self):
        print("I have a car")


eo = son()

eo.flat()
eo.land()
eo.car()
------------------------------------------------------------------------------------------
4.Hierarchical Inheritance:
    Parent
      |
 -------------
  |           |
 Child1   Child2

---> Multiple Child classes inherits from a single parent.
Ex:
class father:
    def land(self):
        print("I have 10A Land")

class Tarun(father):
    def sa(self):
        print("I am jobless")

class Likhi(father):
    def pa(self):
        print("I have job")


ow = Tarun()
ow.land()


pw = Likhi()
pw.land()

-----------------------------------------------------------------------------------------
5.Hybrid Inheritance:

--> This is the combination of two or more types of inheritance.

EX:
class A:
    def some(self):
        print("CLass A")

class B(A):
    def so(self):
        print("Class B")

class C(A):
    def all(self):
        print("Class C")


class D(B,C):
    def al(self):
        print("Class D")



ow = D()

ow.some()
ow.all()
ow.so()
ow.al()


-----------------------------------------------------------------------------------------

super() Method:
---------------
---> super() is used to access methods and constructor of the parent class from the child class.

Ex:
---
class parent:
    def display(self):
        print("Method Parent")

class child(parent):
    def display(self):
        super().display()
        print("Method child")


ow = child()
ow.display()

-------------------------------------------------------------------------------------------
# 1. Single Inheritance

class library:
    def poetrybooks(self):
        print("I have 5 poetry books")
    def Sci_fi_Books(self):
        print("I have 10 Science fiction books")

class Student(library):
    def student(self):
        print("I am using library now")


ow = Student()
ow.Sci_fi_Books()

# 2. Multiple Inheritance:

class library:
    def poetrybooks(self):
        print("I have 5 poetry books")
    def Sci_fi_Books(self):
        print("I have 10 Science fiction books")

class studyroom:
    def Tables(self):
        print("I have 1 table")
    def Chairs(self):
        print("I have 1 Chair")

class Student(library,studyroom):
    def student(self):
        print("I am using library now")

ow = Student()
ow.Sci_fi_Books()
ow.Tables()

-----------------------------------------------------------------------------------------------------------
'''

class person:
    def __init__(self,name):
        self.name = name


class stu(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name : {self.name}" )
        print(f"Roll No: {self.roll}")


any_ = stu('Tarun',102)
any_.show()
























