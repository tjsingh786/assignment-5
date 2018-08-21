# ques-1
year = int(input("Please Enter the Year"))
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print("%d is a Leap Year" % year)
else:
    print("%d is Not the Leap Year" % year)

# ques-2
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
if (length == breadth):
    print("square")
else:
    print("rectangle")

# ques-3
x = int(input("enter the age of first person"))
y = int(input("enter the age of second person"))
z = int(input("enter the age of third person"))
if (x > y):
    if (x > z):
        print("x is eldest")
    else:
        print("z is eldest")
else:
    if (y > z):
        print("y is eldest")
    else:
        print("z is eldest")
if (x < y):
    if (x < z):
        print("x is youngest")
    else:
        print("z is youngest")
else:
    if (y < z):
        print("y is youngest")
    else:
        print("z is youngest")


# ques-4)
age=int(input("enter the age:"))
gender= input("enter the gender:")
marital= input("enter the marital status:")
if (gender == 'female'):
    print("she will work only in urban areas")
elif (gender == 'male' and age > 20 and age < 40):
    print("he may work in anywhere")
elif (gender == 'male' and age > 40 and age < 60):
    print("he may work in urban areas only")
else:
    print("ERROR")

# ques-5)
x = int(input("enter the quantity "))
price=x*100
discount=10/100
if (price > 1000):
    price=price-discount
    print("cost is:",price)
else:
    print("cost is:",price)

#LOOPS
#Q.1
integers=[]
for i in range(10):
    value=int(input('Enter value:'))
    integers.append(value)
print(integers)

#ques-2
'''x=True
while True:
    print("hello world")'''

#ques 3
l1=[]
l2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter element:'))
    l1.append(b)
print('List:',l1)
for i in range(a):
    c=l1[i]*l1[i]
    l2.append(c)
print('List of Squared element:',l2)

#ques 4
list=['tajinder',1,2.5,'nikunj',2,3.5,'akshat',3.1,4.5]
a=[]
b=[]
c=[]
for i in list:
    if(type(i)==int):
       a.append(i)
    elif(type(i)==str):
       b.append(i)
    elif(type(i)==float):
       c.append(i)
print(a)
print(b)
print(c)

#ques 5
num1 = 1
num2 = 100
for num in range(num1, num2 + 1):
    if num1 > 1:
        for i in range(2, num):
            if num % index == 0:
                break
            else:
                print(num)
#ques-6
for i in range(4):
   print('\n')
   for j in range(0,i+1):
     print('*' , end= ' ')

#ques-7
list1=[]
list2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digit:'))
    list1.append(b)
search=int(input("Enter value to search:"))
list1.remove(search)
print(list1)