'''
DAY3 of my python class

Program to convert 24H clock to 12H clock using only keywords

time = input("Enter time : ")

parts = time.split(":")
hour = int(parts[0])
mins = int(parts[1])

print(f"{time} is converted into {hour - 12} : {mins} pm")

---------------------------------------------------------------
List:

--> List is collection of different data types
--> [] and separted by ","
--> List is mutable
EX:
any = [1,"Python",[1,2]]
print(any)
print(type(any))
print(any[2][2][1][8])

EX2: any = [1,"Python",[1,2,[34,"this is python 3rd class",78],"Python is a language",89],34,[3,4]]
     print(any[2][4])
-----------------------------------------------------------------
METHODS:

1. append():
--> This method is used to add new item into list, and it will in the last index position.
Syntax: Variable_name.append(item)
EX:
any = [1,2,3]
any.append(6)
print(any)
any.append([20,70])
print(any)
-----------------------------------------------------------

Immutable:
--> Could not able to modify on that particular variable
Ex: INT,STR
so = "python is a language"
print(so.replace("python","Java"))
print(so)
-------------------------------------------------------------
Mutable:
--> Can able to modify on that particular variable.
eg: List
any = [1,2,3]
any.append(6)
print(any)
--------------------------------------------------------------
2.extend():
--> This method is used to add itterable into list, and it will in the last index position, each  value or substring is each index in the list
Syntax:
variable_name.extend(itterable)
-------------------------------------------------------------
3.pop():
--> Used to remove the item from the list, but will mentio her index position in the pop method
EX:
any = [1,2,3,4,5,6]
print(any.pop())
any.pop(0)
print(any)
-------------------------------------------------------------
4.remove():
--> used to remove the item from the list with direct value assigned as "X"
syntax:
--> variable_name.remove()

'''







