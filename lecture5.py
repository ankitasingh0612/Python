# i=1
# while i<=100:
#     print("hello",i)
#     i+=1
    
# i=5
# while i>=1:
#     print("hrlll",i)
#     i-=1
    
    
    #break and continue
    
    #break is used to terminate the loop when encountered.
    
    
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
    
    #continue is used to terminate the current iteration and continues to next iteration(skip)

# i=0
# while i<=5:
#     if(i==3):
#        i+=1
#        continue
#     print(i)
#     i+=1   
    
    
# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# i=1
# while i<=20:
#     if(i%2 !=0):
#         i+=1
#         continue
#     print(i)
#     i+=1
    
    
 #for loop are used  for sequential traversal
 
# veg=["potato","brinjal","cucumber"]

# for value in veg:
#     print(value)  
   
   
# num=[1,3,4,6,8,5]
# for val in num:
#     print(val) 
    
    
# tup=(1,4,6,67,43,5)
# for val in tup:
#     print(val)


# str="apnacollege"
# for char in str:
#     if(char=="o"):
#         print("o found")
#         break
#     print(char)
    
# else:
#     print("END")
    

#range function return a sequence of  numbers and starting with 0 by default and incremented by 1


# for val in range(6):
#     print(val)
# print(range(8))


# seq=range(10)
# print(seq[0])
# print(seq[3])
# print(seq[4])
# print(seq[6])


# seq=range(6)
# for i in seq:
#     print(i)



# for i in range(10):#range(stop)
#     print(i)
    

# for val in range(2,6): #range(start,stop)
#     print(val)
    
    
# for el in range(2,10,2): #range(start,stop,step)
#     print(el)
    
    
# nested loop
# for i in range(1,4):
#     for j in range(1,11):
#         print(j,end="")
#     print() # this is used for printing in next line



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
        
        

# for j in range(1,10):
#     print("9"*j ,end="")
#     print()


# for i in range(1,10):
#     print("*"*i, end="")
#     print()
    
    
# for i in range(7,0,-1):
#     print("*"*i,end="")
#     print()