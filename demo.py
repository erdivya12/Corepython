'''x = "mobile"
print (x)
'''
'''import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%B"))

print(x.strftime("%a"))
print(x.strftime("%b"))
'''
#######functions
'''def sum(a,b,c):
    D=a+b+c
    print("sum of a,b,c=",D)
sum(20,40,45)'''

'''def multiply(a,b):
    c=a*b
    print(c)
multiply(12,14)'''

'''def divide(a,c):
    D=a%c
    print(D)
divide(12,4)'''
'''def subtract(a,b):
    return a-b
subtract(34,12)'''
'''def greet():
    print("hello divya")

greet()
multiply(12,4)
sum(13,78,45)'''



'''def subtract(c,d):
    a=c-d
  print(a)
def add(c,d):
    a=c+d
    print(a)
def multiply(c,d):
    a=c*d
    print(a)
    int=input("enter the action"(1,2,3))
    if i in int:
        print(a-b,subtract(a,b))'''

###typecasting
'''a=3.14
b=int(a)
print(b)
num=123
str_num=str(num)
print("value of str_num after typecasting from int to string:",str_num)
print(type(str_num))
str_num="456"
num=int(str_num)
print("value of num after typecasting from string to int:",num)'''
'''def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0
        return "Error! Division by zero!"
    else:
        return x/y
def calculator():
    print("select operation:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("divide")
    
    choice = input("Enter choice(1/2/3/4):")
    
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    
    if choice=='1':
        print("result:",add(num1,num2))
    elif choice=='2':
        print("result:",subtract(num1,num2))
    elif choice=='3':
        print("result:")'''
print("Hello World.......")#print any message between these("") codes

a=13#printing int numbers
b=12#assiging 12 in variable b...(a,b)here a&b is variable
print(a)
print(b)

a="divya"#string data type ("") these indicates data is string
print(a)

b='a'#('')these indicates data is char
print(b)

###addition of two numbers
a=98
b=23
c=a+b#c is another variable
print("perform addition of a,b:",c)# here(,)is concatenation this coonnect string &values

###subtraction of two numbers
a=4
b=20
c=a-b
print("perform subtraction of a,b:",c)

###multiplication of two numbers
a=2
b=50
c=a*b
print("perform multiplication of a,b:",c)

###division of two numbers
a=7
b=20
c=a/b
print("perform division of a,b:",c)

###standard data type list
list=["divya","ram",'a','b',1,2,3]#name in ""& char in '' & number direct
print(list)

###standdard data type tuple
tuple=("divya",1,4,6,8)
print(tuple)
print(type(tuple))#here define the class is tuple
#while loop
num=0
while(num<=10):
    print(num)
    num+=1
#reverse upper program
num=10
while(num>=0):
    print(num)
    num-=1

#if else statement
l1=[1,2,3,4,"divya",'a']
l2=[2,3,4]
if(l1<l2):
    print("l1 have large element as compared to l2:")
else:
    print("l2 have large element as compared to l1:")















