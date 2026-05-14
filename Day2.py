'''
                                                                                                            Day2 of my python
-----------------
Operators:
---------------------------------------
1. Arithmetic Operators
EX: +,-,/,//,%,**
print(a+b)
--------------------------------------
2. Assignment Operators
EX: = , +=,-=,%=,*=
--------------------------------------
3.Comparision Operators
EX: (==)*,!=,>=,<=,>,<
--> a = [1,2]
    b = [1,2]
    print(a==b)
    True
Note: "==" Looks for both values equal or not
----------------------------------------
4. Identity Operators
Ex: (is)*, is not
--> a = [1,2]
    b = [1,2]
    print(a is b)
    False (Because for variables the id is differently allocated)
Note--> "is" Operator looks for the Object is same or not
--------------------------------------
5. Logical Operators
Ex: and--> This is operator check the both should be True
    or --> This is operator check the weather one should be True

a = 15

if a % 3 == 0 and a % 5 == 0:
    print(True)
else:
    print(False)

a = 5

if a % 3 == 0 or a % 5 == 0:
    print(True)
else:
    print(False)
--------------------------------------
6. Membership Operators:
in
not in
-------------------------------------
7.Bitwise Operators:
&,|,<<,>>
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


a = 9 #immutable
b = 7.0
print(a+b)


                                                                                                    Strings

                                                                                                    
string---> '',"",''' '''
String is sequence of characters that are enclosed in '',"",''' '''. and string is immutable data type

Ex: phew = "+.*4$#"
------------------------------

Methods:
-------
replace()
Syntax ---> Variable_name.replace("old_string","new_string")
EX:
ade = "Python is a language"
print(ade.replace("Python", "Java"))
print(ade)
----------------------
split()
---> Used to separate in parts, and split based on the sub string where
before substring is one index and after is another index in the list
Syntax ---> Variable_name.split("sub_string")
-----------------------------------------------------------------------------------------------------------------

In-Built Functions:
len() --> get number of items , substring
Ex:
any = "Python is a language"
print(len(any))
-------------------------------------
Slicing()--> can give the access to get particular index from the string
Syntax--> Variable_name[starting index : ending index]
Ex:
any = "Python is a language"
print(any[3:10])

indexing
--------
--->Used to get substring present in that index position
Syntax --> Variable_name[index_position]
EX:
any = "Python is a language"
print(any[8])

---------------------------------------------------------------
count()
----------------
join()

'''








