str1="hi everyone"
str2="my name is ankita singh"
str3="hello"
str4="world"
print(str1,str2)
print(str1+str2)
print(str3+str4)
print(len(str1))

#indexing
print(str1[4])

#slicing
print(str1[3:7]) #inding index is not included
print(str2[11:17])
print(str3[2:])
print(str2[-6:-1])

#string function
print(str1.endswith("ne")) #return true if string ends with substr
print(str1.endswith("sp"))

print(str2.capitalize())#gives new string doest not change original str
print(str2)
print(str1.capitalize())

print(str2.replace("a","b"))#replace all the old str
print(str1.replace("everyone","dostooo"))

print(str1.find("hi")) #return first index of first occurrence
print(str2.find("ankita"))

print(str3.find("name")) #it gives -1 when not found in str


print(str2.count("a")) #count the occurrence of str
print(str2.count("s"))

#conditional Statement
light="pink"
if(light=="green"):
    print("go")
elif(light=="red"):#elif  executes when if statement is wrong
    print("stop")   
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")
print("end of code")


num=5

if(num>2):
    print("greater than 2")
if(num>3):
    print("greater than 3")
    
    
marks=75
if(marks>=90):
    print("grade A")
elif(90>marks>=80):
    print("grade B")
elif(80>marks>=70):
    print("grade C")
elif(marks<70):
    print("garde D")
 
 #nesting
age=16
if(age>=18):
    if(age>=80):
       print("can not  drive")
    else: 
        print("can drive")  
else:
    print("cannot drive")
    

string="helloworld"
print(string[::-1])



#Shorthand if statement(used when only one statement needs to be executed inside the block )
marks=92
if marks>=90: print("you will get a new phone")

#shorthand if -else statement
marks=89
print("you will go trip ") if marks>=90 else print("no phone for a month")



#bitwise operator
# 1.AND operator
print(bin(10))
print(bin(6))

a=10
b=6
print(bin(a&b))

#2.or operator
a=10
b=8
print(bin(a|b))


#3.xor operator(same same gives zero rest one)
a=10
b=8
print(bin(a^b))


#4.left shift
print(10>>2)
print(10>>1)


#5.right shift
print(10<<2)


