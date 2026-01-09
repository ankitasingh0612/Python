# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def average(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name," your average score is:",sum/3)
             
# s1=student("ankit",[87,98,77])
# s1.average()

# s2=student("anil",[67,87,84])
# s2.name="akhil"# directly change the attribute value
# s2.average()



class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited..")
        print("total balance=",self.get_balance())
        
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited..")
        print("total balance=",self.get_balance())
        
    def get_balance(self):
        return self.balance
        
acc1=account(100000,123)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(4000)
acc1.debit(500)