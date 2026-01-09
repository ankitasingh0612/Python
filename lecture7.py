#file i/o in python(python can be used to perform operation on a file)

#open,read,&close file
# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()


# f=open("demo.txt","r")
# data=f.read(5) #read entire file
# print(data)
# print(type(data))
# f.close()


# f=open("demo.txt","r")
# line1=f.readline() #read line by line
# print(line1)

# line2=f.readline()
# print(line2)
# f.close()


# f=open("demo.txt","r")
# data=f.read() #gives empty value because it reads all data and cursor move to the end of the file
# print(data)
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()


#writing a file
# f=open("demo1.txt","w") #overwrites the entire file
# f.write("hii how are you")
# f.close()

# f=open("demo1.txt","a") #add to the new file
# f.write("\ni am fine")
# f.close()


#creating a file automatically with w and a
# f=open("sample.txt","w")
# f.close()
# f=open("sample1.txt","a")
# f.close()

# f=open("sample.txt","r+") #overwrite from startings
# f.write("abc")
# print(f.read())
# f.close()

# f=open("sample.txt","a+") #add to end of file
# print(f.read())
# f.write("abc")
# f.close()

# f=open("sample1.txt","w+")#file will be open in truncated mode so all the data will lost
# print(f.read())
# f.write("asdfgh")
# f.close()


#with syntax
# with open("demo2.txt","r") as f:
#     data=f.read()
#     print(data)
# with open("demo2.txt","w") as f:
#     f.write("helllooo")


#deleting  a file(using os module)

# import os
# os.remove("sample2.txt")

    