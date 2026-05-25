'''
----------------------------------Day11 of python class----------------------------

-> Assert :
--> this is debugging statement used to test wheather a condition is True or not
EX:
num1 = int(input())
num2 = int(input())

assert num1 > num2, "Number1 is greater than Number2"
print("True")
--------------------------------------------------------
FUNCTIONS:
-> A function is block of code which only excutes when it is called
--> we can pass data, known as parameters into a function
--> to avoid repeated lines in code


def function_name(parameters):
    ------------
    ------------
function_name(arguements)

EX:
num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(num)
even(130)
-----------------
Ways to  pass arguements
------------
1. Required arguements
--> A function must be called with the same parameters
EX1:
num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(num,90)
EX2:
num1 = 9
def even(num1,num2,num3):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(num1,90)

-----------------------------------
2. Default Arguements:
 --> Default values is defined by parameters even though it will take from arguements.

EX:

def even(name = "Tarun", age = 29,salary = 75000):
    print(name)
    print(age)
    print(salary)
even("Kakara",100,100000)
---------------------------------------
Keyword arguements:
---> you can send arguements with key = value syntax. By this, the order of arguements doesn't matter.
Ex:
def even(age,salary,name):
    print(name)
    print(age)
    print(salary)
even(name = "Kakara", age = 100,salary = 100000)
----------------------------------------
Variable length arguements:
---> Adding a star(*) before the parameter name in the function, recieve a tuple of argumennts and can access items with indexes

Ex:
def even(*name):
    print(name[1])
even("Tarun","Kakara","Naveen","Nagendra")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Sum of two numbers -

def sum(a,b):
    print(a+b)
sum(3,4)
---------------------------
2. checking whether number is even or odd:

num = int(input())
def amd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("odd number")
amd(num)
---------------------------
3. Prime number range(1,100)-
for i in range(2,101):
    for j in range(2,i):
        if i % 2 == 0:
            break
    else:
        print(f"{i} is a prime number")

With using function:
is_prime = int(input())

def ddsn(is_prime):
    for i in range(2,101):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(f"{i} is a prime number")
ddsn(is_prime)
--------------------------------------------






'''


























































