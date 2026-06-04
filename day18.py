'''
                                    Day18 - Python class


OOPS----> Object Oriented Programming System

1.Class--

--> a Class is a blueprint or a template used to create object
EX:
class student:
    name = "Tarun"
-------------------------------------------------------------------
2.Object:

--> an Object is an instance of class

Ex:
class student:
    name = "Tarun"
s1 = student()

print(s1.name)
------------------------------------------------------------------
Attributes:

--> attributes are variables which is belongs to class or an object.

EX:
class student:
    name = "Tarun"
    age = 23
s1 = student()

print(s1.name)
print(s1.age)
------------------------------------------------------------------
Methods:

--> Methods which are defined functions inside the class
EX:
class PFS_DA():
    def python(self):            #This is function which inside the class.
        PFS_DA = 'Batch_03'
        print("This is python and DA batch")
    def flask(self):             #this is function which inside the class.
        flask = "Batch_03"
        print("This is only for pyton batch")
sdw = PFS_DA()

sdw.python()
------------------------------------------------------------
Constructors:

---> A constructor is a special method that is automatically called when object
is created.

EX:
class ATM:
    def __init__(self,name,balance):
        self.balance = balance
        self.name = name

    def Bal_check(self):
        print(f"{self.name} your total balance is {self.balance}")

card = ATM(balance = 50000, name = "Tarun")
card.Bal_check()
--------------------------------------------------------------

Access Specifiers:

1. Public:
--> This can be accessed from anywhere in the program
eg:
class  stu:
    name = 'Tarun'

sq = stu()
print(sq.name)
------------------------------------------------------------
2. Protected:
--> This is represented using a Single underscore(_)
eg:
class  stu:
    _name = 'Tarun'

sq = stu()
print(sq._name)

-------------------------------------------------------------
3. Private
-->This is represented using a Double underscore(__)
eg:
class  stu:
    __name = 'Tarun'

sq = stu()
print(sq._stu__name)
----------------------------------------------------------------

Encapsulation:
--> Is the process of binding data and methods together

EX:

class bank:
    def __init__(self,balance):
        self.__balance = balance
    def depo(self,amount):
        self.__balance += amount
    def get_bal(self):
        return self.__balance
acc = bank(10000)
acc.depo(100000)
print(acc.get_bal())
--------------------------------------------------------------------
'''



























    


































































