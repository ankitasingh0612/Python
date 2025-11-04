# #list
# #list are mutable in python whereas string are immutable and tuple is also immutable
# marks=[94.5,68.5,67.8,45.9,47.6]
# print(type(marks))
# print(marks)
# print(marks[2])
# print(len(marks))
# marks[4]="ankita"
# print(marks)


# #list slicing
# marks=[87,95,86,58,86,93]
# print(marks[1:5])
# print(marks[:4])
# print(marks[2:])
# print(marks[-5:-2])


# #list method
# list=[4,6,9,"ankita"]
# list.append("anjali")# append method add one element at the end
# print(list)

# num=[3,5,2,4,8,6]
# num.sort()# sort in accending order
# print(num)

# num.sort(reverse=True)# sort in descending order
# print(num)

# num1=[2,5,9,"ankita",8.6,"anjali"]#reverse the list
# num1.reverse()
# print(num1)

# num2=[4,2,"ank",8,9,10,"anj"]
# num2.insert(5,"annu")#insert element at index
# print(num2)


# list1=[2,1,3,1,5,3,1]
# list1.remove(1) #removes first occurrence of element
# print(list1)


# list1.pop(0)#removes element at index
# print(list1)


#tuples in python

# tup=(3,6,2,7,1,9)
# print(type(tup))
# print(tup[3])

tuple=(2,)#commas are compulsory whe one value in tuple
tuple1=(2)
print(type(tuple))
print(type(tuple1))


#slicing in tuple
num=(4,5,7,2,8,2,7,2)
print(num[1:4])
print(num[:4])
print(num[1:])
print(num[-3:])
print(num[-4:-1])
print(num.index(7))#return index of first occurrence
print(num.count(2))#counts total no of occurrence