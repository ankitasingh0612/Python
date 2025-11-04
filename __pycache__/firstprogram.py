name="ankita"
age=20
price=25.99

print("my name is",name)
print("my age is:",age)

# datatypes
print(type(name)) 
print(type(age))
print(type(price))
old=True
a=None
print(type(old))
print(type(a))

#sum of two no.
a=10
b=3
c=a+b
print(c)
print(a+b)


#comments

"""
print("i am a ankita singh ")
print("hi")
print("hello")
"""



#arithmetic operator
a=10
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#remainder
print(a**b) #power

#relational/comparision operator
a=60
b=30
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

#assignment opertor
a=50
a+=10
# a-=10
# a*=10
# a/=10
# a%=10
# a**=10
print(a)

#logical operator
#1.not operator(it gives opposite vlaue and works on single value)
a=15
b=10
print(not True)
print(not False)
print(not(a>b))
#2and operator(it gives true value when both values are true and works on multiple value)
val1=False
val2=True
print(val1 and val2)
# 3 or operator(it gives true value when atleat one values are true and works on multiple value)
print(val1 or val2)
print(a>=b or a==b)
print(a<=b and a==b)

#type conversion(when we convert one type of variable into another)
# string ko floating value m add karna allow nhi hota h
# a="10"
# b=10.5
# print(a+b) #it gives eeror
a=int("4")#type casting-its works when valid no.is
b=20
c=20.5
print(a+b)
print(a+c)
print(str(c))

#inputs in python
#input gives output as a string always
val=input("enter your name")
print(type(val),val)
val1=float(input("enter the value"))
print(type(val1),val1)

name=input("enter ur name")
age=int(input("enter ur age"))
marks=float(input("enter ur marks"))
print(type(name),name)
print(type(age),age)
print(type(marks),marks)


