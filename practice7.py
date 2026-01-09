# with open("practice.txt","w") as f:
#     f.write("hi everyone\nwe are learning file input output\n")
#     f.write("using java.\n i like programming in java")

# #replace all 
# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("java","python")
# print(new_data) 

# with open("practice.txt","w") as f:
#      f.write(new_data)  


#file exists or not
# word="xlearning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")
        
        #or
# def check_for_word():
#   word="learning"
#   with open("practice.txt","r") as f:
#       data=f.read()
#       if(data.find(word)!=-1):
#          print("found")
#       else:
#          print("not found")
# check_for_word()


# def check_for_line():
#    word="learning"
#    data=True
#    line_no=1
#    with open("practice.txt","r") as f:
#       while data:
#          data=f.readline()
#          if(word in data):
#             print(line_no)
#             return 
#          line_no +=1
#    return -1
# check_for_line()


# def check_for_line():
#    word="programming"
#    data=True
#    line_no=1
#    with open("practice.txt","r") as f:
#       while data:
#          data=f.readline()
#          if(word in data):
#             print(line_no)
#             return
#          line_no +=1
#    return -1
# check_for_line()


# with open("prac.txt","r") as f:
#    data=f.read()
#    print(data)
#    num=""
#    for i in range(len(data)):
#       if(data[i]==","):
#          print(num)
#          num=""
#       else:
#          num+=data[i]
            
            
            
# count=0
# with open("prac.txt","r") as f:
#    data=f.read()
#    print(data)
#    num=data.split(",")
#    for val in num:
#       if(int(val)%2==0):
#          count+=1
# print(count)
         