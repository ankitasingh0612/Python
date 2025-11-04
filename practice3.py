# movies=[]
# movie1=input("enter your first favourite movie name")
# movie2=input("enter your second favourite movie name")
# movie3=input("enter your third favourite movie name")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)


# list1=[1,2,1]
list1=[1,2,3]
c=list1.copy()
c.reverse()
if(c==list1):
    print("palindrome")
else:
    print("not palindrome")


list=["m","n","n","m"]
b=list.copy()
b.reverse()
if(b==list):
    print("palindrome")
else:
    print("not palindrome")



tup=("C","D","A","A","B","B","B","A")
print(tup.count("A"))
print(tup.count("B"))


tuple=["C","D","A","A","B","B","B","A"]
tuple.sort()
print(tuple)