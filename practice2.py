# name=input("enter your name")
# print(len(name))
# print(name.find("k"))
# print(name.count("i"))
# print(name.endswith("t"))
# print(name.capitalize())
# print(name.replace("ankita","anjali"))


# str="hi, $hyam how are you $uper anki$hfd"
# print(str.count("$"))



# num=int(input("enter the no."))
# if(num%2==0):
#     print("even no.")
# else:
#     print("odd no.")


# num1=int(input("enter the  first no"))
# num2=int(input("enter the second no"))
# num3=int(input("enter the  third no"))
# if (num1>=num2 and num1>=num3):
#     print("num1 is greatest")
# elif( num2>=num3):
#     print("num2 is greatest")
# else:
#     print("num3 is greatest")


# x=int(input("enter the no."))
# if(x%7==0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")
    
    


# write a program to create a area calculator
# print(".....AREA CALCULATOR....")
# print("""press1 you will get area of square
#       press 2 you will get area of rectangle
#       press 3 you will get area of circle
#       press 4 you will get a area of triangle""")

# choices=int(input("enter a no. btw 1-4:"))
# if choices==1:
#     side=float(input("enter the  length of one side"))
#     area=side**2
#     print("area of square is:",area)
    
# elif choices==2:
#     len=float(input("enter the length of rectangle"))
#     bre=float(input("enter the breadth of rectangle"))
#     area=len*bre
#     print("area of rectangle is:",area)

# elif choices==3:
#     r=float(input("enter the radius of circle"))
#     area=3.14*r*r
#     print("area of circle is:",area)

# elif choices==4:
#     base=float(input("enter the base of triangle"))
#     height=float(input("enter the height of triangle"))
#     area=0.5*base*height
#     print("area of triangle is:",area)
# else:
#     print("invalid input")
    
    
    
#WAP to check a passed letter is vowel or not
# letter=input("enter the letter:")
# if (letter in "aeiou") or(letter in "AEIOU"):
#     print("it is vowel")
# else:
#     print("it is not vowel")
    
    
# WAP to  check the no is 1 digit,2 digit ,3 digit ...up to 5 digit
num=int(input("enter the no"))
if num>=0 and num<=9:
    print("the no is single digit")
elif num>=10 and num<=99:
    print("the no is 2 digit")
elif num>=100 and num<=999:
    print("the no is 3 digit")
elif num>=1000 and num<=9999:
    print("the no is 4 digit")  
elif num>=10000 and num<=99999:
    print("the no is 5 digit")
else:
    print("nothing")
    
    