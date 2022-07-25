----------------Python Cheat Sheet -------------
1) int(3.14) 
2) float(2) 
3) a=2+3j
complex(2)   
4) Str(100) Would convert the Int into string

5) pow(x,y)
6) divmod(x,y)
7) abs(x)
8) import math
math.factorial(x)
 
9) Plus Operator : "+"

----When You need to Concat Two String 

a=100
b='$'

print(b+str(a))

o/p : $100

----When two Int values needs to be added 

x=10
x=x+2
print(x)

o/p : 12


-------Example -------

a='Hello'
b='Welcome to the Python Master Class'

print(a + '    ' +b)


=======================05/14============

Factorial : 3
           : 3*2*1 
           
           :5 
           : 5*4*3*2*1
           
           


10) Checking the data types of An Varibale /Expresion :

type(10)
int

type(a)
str

type(12.5)
float


11)  Assigning the multiple values into varible 


a=5
a=10
print(a)

--10


12) Interchanging the variable values  , But both variable got the values of Variable y


x,y = (100,200)
print('x old value is :' ,x)
print('y old value is :' ,y)
print('Assigning the y value to x')
x=y   
print('Assigning the x value to y')
y=x    
print('x New value is :' ,x)
print('y New value is :' ,y)


13) Interchanging the variable values betweeb x and y :


x,y = (100,200)
print('x old value is :' ,x)  --> 100
print('y old value is :' ,y)  --> 200
print('Assigning the y value to x')
temp=x  --> temp --> 100
x=y     ---> x --> 200

print('Assigning the x value to y')
y=temp   ---> y --> 100
print('x New value is :' ,x)
print('y New value is :' ,y)


14) Divison , Quotient and Remainder 

a=13
b=4

y=a/b
print('Diviosn of a and b:' ,y) # Float output

x=a//b
print('Quotient of a and b:' ,x) 

z=a%b
print('Mod/Remainder of a and b:' ,z)

15) 

	Operation	Description
	x==y		 x is equal to y
	x != y	 	 x is not equal to y
	x > y 		 x is greater than y
	x < y 		 x is less than y
	x >= y 		 x is greater than or equal to y
	x <= y 		 x is less than or equal to y


16) Additional Operator check

x > 0 and x < 10 

n%2 == 0 or n%3 == 0 


17)

a=13
b=4

y=a/b
print('Diviosn of a and b:' ,y) # Float output

x=a//b
print('Quotient of a and b:' ,x) 

z=a%b
print('Mod/Remainder of a and b:' ,z)


18 ) Chapter 9,10 --> page 19 for Addiotinal Logic


19) Chapter 9,10  ---> Operator Precedence --> Page 23 --> BODMAS





================06/04=============I/O Ops==============Input /Split/

20 )
res = input('What is your favorite programming language: ')

21) 
year = int(input(“What is your age?” ))  ---> Error Coming while passing float value as input

-------Conclusion ------

year = int(float(input('What is your age?' )))
print(year)


Name = str(input('What is your age?' ))
print(Name)





22) ----Split Method ---


reply = input(" Enter x and y, separated by spaces:" )
var1 = reply.split( ) 	           # returns a list of strings, as separated by spaces
var2= reply.split(',' )            # returns a list of strings, as separated by comma
var3 = reply.split('#')            # returns a list of strings, as separated by #
x = int(var1[0])
y = int(var1[1])
z = int(var1[2])
print(x,y,z)




reply = input(" Enter x and y, separated by spaces:" )
var1 = reply.split( ) 	           # returns a list of strings, as separated by spaces
var2= reply.split(',' )            # returns a list of strings, as separated by comma
var3 = reply.split('#')            # returns a list of strings, as separated by #
x = int(var2[0])
y = int(var2[1])
z = int(var2[2])
print(x,y,z)


reply = input(" Enter x and y, separated by spaces:" )
var1 = reply.split( ) 	           # returns a list of strings, as separated by spaces
x = int(var1[0])
y = int(var1[1])
z = int(var1[2])
print(x,y,z)



reply = input(" Enter x and y, separated by Comma:" )
print(reply)
var1 = reply.split(',')   # returns a list of strings, as separated by comma
x = int(var1[0])
y = int(var1[1])
z = int(var1[2])
print(x,y,z)


reply = input(" Enter x and y, separated by #:" )
var1 = reply.split('#')   # returns a list of strings, as separated by #
x = int(var1[0])
y = int(var1[1])
z = int(var1[2])
print(x,y,z)



23) 
print("Is Python a dynamic language?",end="\nPython")

print("Is Python a dynamic language?\n",end="Python")

print("Is Python a dynamic language?\t",end="Python")



24) 
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")


input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any number ")
check_user_input(input2)

input2 = input("Enter the last number ")
check_user_input(input2)



25 ) 

count = int(input("Enter the count: "))
theSum = int(input("Enter the sum: "))
if count > 0 and theSum // count > 10:
	print("average > 10")
else:
	print("count = 0 or average <= 10")




--------------------.format-----------------
26) 


print("Hello {}, your balance is {}.".format("Adam", 230.2346))

print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))


print("Hello {0}, your balance is {1}.".format(230.2346,"Adam"))

print("Hello {0}, your balance is {balance}.".format("Adam", balance=230.2346))



--------------------06/11----------------If then Else Condition

27) 

print('First Condition Statement')
x=3
y=4

if x>y:
    print('X is greater than Y')


print('Last Statement of Script without checking If Condition')    
 
 
 
 28)
 
  print('First Condition Statement')
x=3
y=4

if x>y:
    print('X is greater than Y')
elif x<y:
        print('X is lesser than Y')


print('Last Statement of Script without checking If Condition')  
 
 
 
 29) 
 
 print('First Condition Statement')
x=5
y=4
z=2

if x>y:
    print('X is greater than Y')
    if z<y:
        print('Print 2nd If condition ')


print('Last Statement of Script without checking If Condition') 


30) 
    
    print('First Condition Statement')
x=5
y=4
z=6

if x>y:
    print('X is greater than Y')
    if z<y:
        print('Print 2nd If condition ')


print('Last Statement of Script without checking If Condition')  
    
    
    
31) Printing multiple lines of comments 
Var_1="""
This is Python master class
This is with Data Science
Focus on class
"""

print(Var_1)


--------------------06/12---------------------------

----While Loop---
while condition:
	body

----Range -------

range(start, End , step)

x = range(3, 20, 2)

----For Loop ----
for var in Expression/Logic:
statements	



-------While loop -----------------

32) 

n=int(input("Enter your Age "))
type(n)
while n > 0:
    print('Number is ',n)
    n = n-1
    
print('Blastoff!')
    

o/p:
5
4
3
2
1
Blastoff

33) 

n=int(input("Enter your Age "))
type(n)
while n > 0:
    print('Number is ',n)
    n = n-1  
    print('Blastoff!')
    
o/p:

Enter your Age 5
Number is  5
Blastoff!
Number is  4
Blastoff!
Number is  3
Blastoff!
Number is  2
Blastoff!
Number is  1
Blastoff!

34) Finite While Loop which prints nothing because we have not defined Count initial Value.

while count < 5:    
    print(count)   
    count = count + 1

35) Infinite Loop : Below example would go into infinite loop reason is 5 is true all the time

while 5:    
    print(count)   
    count = count + 1
    
    
36) 

count=0
while count in range(5):    
    print(count)   
    count +=  1
    
o/p :

0
1
2
3
4


--------------Range -----------------------

33) 
Range_variable = list(range(6))
print(Range_variable)

[0, 1, 2, 3, 4, 5]


34) 
Range_variable = list(range(2, 24, 3))
print(Range_variable)


35) 

Range_variable = list(range(2, -10, -1))
print(Range_variable)

[2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]



36) Starting Point is Positive , End Point is also Positive and Interval is also Positive

Range_variable = list(range(2, 10, 1))
print(Range_variable)

o/p : [2, 3, 4, 5, 6, 7, 8, 9]

37) Starting Point is Positive , End Point is also Positive and Interval is also Negative

Range_variable = list(range(2, 10, -1))
print(Range_variable)

O/p : []  --> Empty List


38) Starting Point is Positive , End Point is also Negative  and Interval is also Positive
Range_variable = list(range(2, -10, 1))
print(Range_variable)

O/p : []  --> Empty List


39) Starting Point is Positive , End Point is also Negative  and Interval is also Negative

Range_variable = list(range(2, -10, -1))
print(Range_variable)

o/p : [2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


40) Starting Point is  Negative, End Point is also Negative  and Interval is also Negative

Range_variable = list(range(-2, -10, -1))
print(Range_variable)


o/p : [-2, -3, -4, -5, -6, -7, -8, -9]


41) Starting Point is  Negative, End Point is also Negative  and Interval is also Positive

Range_variable = list(range(-2, -10, 1))
print(Range_variable)

42) Starting Point is  Negative lesser than end point, End Point is also Negative  and Interval is also Positive


Range_variable = list(range(-20, -10, 1))
print(Range_variable)

43) 


Range_variable = list(range(-11, -10, 1))
print(Range_variable)

[-11]

44) 

Range_variable = list(range(-11, -10, -1))
print(Range_variable)


----------------For Loop--------------------

45) 
x=list(range(2, 10, 1))
print(x)
  
o/p :   [2, 3, 4, 5, 6, 7, 8, 9]
  

  
46) 

x=range(2, 10, 1)
for n in x:
  print(n)
  
o/p :
2
3
4
5
6
7
8
9
  
  
47) 

for n in range(2, 10, 1):
  print(n)
  
 o/p :
2
3
4
5
6
7
8
9

---------While Loop and For Loop------------

for x in range(5):    
	print(x)


--------------Nested For Loop---------

48)  
print('i,j with below')
for i in range(1,3):   
    for j in range(1,4):
        print(i,j)
    
i,j with below
1 1
1 2
1 3
2 1
2 2
2 3

49) 
print('i,j,k with below')
for i in range(1,3):   
    for j in range(1,4):
        print(i,j)
    for k in range(1,5):
        print(i,j,k)
        

i,j,k with below
1 1
1 2
1 3
1 3 1
1 3 2
1 3 3
1 3 4
2 1
2 2
2 3
2 3 1
2 3 2
2 3 3
2 3 4


50) 
print('i,j,k with below')
for i in range(1,3):   
    for j in range(1,4):
        for k in range(1,5):
            print(i,j)
            print(i,j,k)
            
i,j,k with below
1 1 1
1 1 2
1 1 3
1 1 4
1 2 1
1 2 2
1 2 3
1 2 4
1 3 1
1 3 2
1 3 3
1 3 4
2 1 1
2 1 2
2 1 3
2 1 4
2 2 1
2 2 2
2 2 3
2 2 4
2 3 1
2 3 2
2 3 3
2 3 4


51) 
print('i,j,k with below')
for i in range(1,3):   
    for j in range(1,4):
        print(i,j)
        for k in range(1,5):
            j=int(j)
            k=int(k)
            if j==k:
                print(i,j,k)
 
 i,j,k with below
1 1
1 1 1
1 2
1 2 2
1 3
1 3 3
2 1
2 1 1
2 2
2 2 2
2 3
2 3 3


---------------List-------------

52) First_List = [10, 30, 40, 60]
print(First_List[3])

--> 60


53) First_List = [10, 30, 40, 60]
print(First_List[-2])

--> 40

54) Multiple_data_Types=['spam', 2.0, 5, [10, 20]]
print(Multiple_data_Types[3])

---> [10, 20]

----One List can have different kind of data types elements----

55) Multiple_data_Types=['spam', 2.0, 5, [10, 20]]
print(Multiple_data_Types[3][0])

--> 10


56)  Numpy and reshape and Array 

from numpy import * 
a = array(
    [
     ['Mon',18,20,22,17],
     ['Tue',11,18,21,18],
     ['Wed',15,21,20,19],
     ['Thu',11,20,22,21],
     ['Fri',18,17,23,22],
     ['Sat',12,22,20,18],
     ['Sun',13,15,19,16],
     ['Unk',10,10,10,10]
     ]
     )
m = reshape(a,8,5))
print(m)


o/p :

[['Mon' '18' '20' '22' '17']
 ['Tue' '11' '18' '21' '18']
 ['Wed' '15' '21' '20' '19']
 ['Thu' '11' '20' '22' '21']
 ['Fri' '18' '17' '23' '22']
 ['Sat' '12' '22' '20' '18']
 ['Sun' '13' '15' '19' '16']
 ['Unk' '10' '10' '10' '10']]
 
 
 ----Numpy--------------
 
 https://www.tutorialspoint.com/python_data_structure/python_matrix.htm
 https://www.w3schools.com/python/numpy/numpy_array_reshape.asp
 