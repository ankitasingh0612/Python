#function is block of code that perform  specific task

# def  sum(a,b):
#     s=a+b
#     return s
# print(sum(10,30))



# def sub(a,b):
#     s=a-b
#     print(s)
#     return s
# sub(10,3)



# def cal_sum(b,c):
#     return b+c
# s=cal_sum(10,4)
# print(s)



# def avg(a,b,c):
#     av=(a+b+c)/3
#     return av
# print(avg(1,3,2))


#find avg of a no.
# def avg(a,b,c):
#     av=(a+b+c)/3
#     print(av)
#     return av
# avg(1,2,3)



#Recursion(when a function calls repeatedly)
# def show(n):
#     if(n==0):#(base case)
#       return
#     print(n)
#     show(n-1)
#     print("END")
# show(6)


def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n
    
print(fact(5))





