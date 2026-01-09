#Function
# num=[1,2,3,4,5,6]
# print(len(num))

# nums=[1,2,3,4,5,6]
# cities=["gkp","lko","delhi"]

# def print_len(list):
#      print(len(list))
    
# print_len(cities)
# print_len(nums)




# cities=["gkp","lko","delhi"]
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
        
# print_list(cities)



#factorial of n
# def cal_fun(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# cal_fun(4)
        
        

# convert USD to INR
# def converter(usd_value):
#     inr_value=usd_value*83
#     print(usd_value,"USD=",inr_value,"INR")
# converter(1)


# calculate sum of n natural no.
# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1) +n
# sum=cal_sum(4)
# print(sum)


#print all the element in the list
fruits=["mango","litchi","apple","banana"]
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
print_list(fruits)

