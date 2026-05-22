'''
Day9 of my python class\

problem1:
1. table:
num = 9

for i in range(1,11):
    print(f"{num} X {i} =  {i*num}")
--------------------------------------------
2. Palindrome:
s = input("Enter a word: ")

es = ""


for i in s:
    es = i + es

if es == s:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
---------------------------------------------
3.Armstrong numbers:

num = int(input())

rm = 0

lens = len(str(num))

for i in str(num):
    rm += int(i) ** lens
if rm == num:
    print("it is an armstrong number")

else:
    print("It is not an armstrong number")

---------------------------------------------
4. Perfect number:
n = int(input())

s = 0

for i in range(1,n):
    if n % i == 0:
        s += i
if s == n :
    print("It is a perfect number")

else:
    print("It is not a perfect number")
----------------------------------------------
5. Prime number:
num = int(input())

count = 0

for j in range(1,num+1):
    if num % j == 0:
        count += 1

if count == 2:
    print("It is a prime number")

else:
    print("It is not a prime number")
---------------------------------------------
6.pattern 1
s = int(input())

for i in range(1,s+1):
    for d in range(1,i+1):
        print("*",end = "")
    print()
----------------------------------
with alphabates:
s = int(input())

for i in range(1,s+1):
    for d in range(1,i+1):
        print(chr(64 + d),end = "")
    print()
-----------------------------------
wit numbers
s = int(input())

count = 0
for i in range(s,0,-1):
    for d in range(1,i+1):
        count += 1
        print(count,end = " ")
    print()
---------------------------------------------------------
Pyramids
num = int(input())

for j in range(1,num+1):
    print(" "*(num-j), end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()




'''




    
