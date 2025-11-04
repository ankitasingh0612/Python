#dictanary
# info={
#     "key":"value",
#     "age":35,
#     "is_adult":True,
#     "subject":["python","c","java"],
#     "topics":("dict","set"),
#     "marks":94.4,
#     89.4:98.3,
#     ("aa","bb"):"aaaaaaaaaaaa"   #make tuple as key
    
# }
# print(info)
# print(type(info))
# print(info["key"])
# print(info["subject"])
# print(info["topics"])
# info["key"]="name"
# print(info)
# info["marks"]="99.9"
# print(info)


#nested dictionaries
# student={
#     "name":"ankita",
#     "subjects":{
#         "phy":78,
#         "chem":98,
#         "hindi":97,
#         "math":99
#     },
#     "college":"itm"
# }
# print(student)
# print(student["subjects"]["chem"])
# print(student["subjects"])


# #dictionary methods
# print(student.keys())#returns all keys

# print(list(student.keys())) #type casting

# print(len(student))#length of dictaionary
# print(len(list(student.keys())))
# print(student.items())
# pairs=list(student.items())
# print(pairs)
# print(pairs[1])

# print(student.get("college")) #return the value
# print(student.get("school")) #return none
# student.update({"city":"delhi"})#insert the specipied items to the dictionary
# print(student)
# new_dict={"name":"annu","age":65}
# student.update(new_dict)
# print(student)



#sets in python
coll={1,4,5,6,4,5,4,"ank","anj",5}#does not follow order
print(type(coll))
print(coll)
print(len(coll))

cls=set() #empty set
print(type(cls))

#sets method
collection=set()
collection.add(2)
collection.add(4)#adds a element in set
collection.add(5)
collection.add((1,3,4))
# collection.add([1,2,3])
collection.remove(5)#remove the element in set

collection.clear()# #empty the set

# collection.remove(6)
print(collection)


std={"hello","hi","apana","anj"}
print(std.pop())#randomly pop the element
print(std.pop())
print(std.pop())

set1={1,4,3,4,6,6}
set2={"hello","anj",4,6,5,3}
print(set1.union(set2)) #combines both set values and return new
print(set1)
print(set2)
print(set1.intersection(set2)) #combines common values and return new


