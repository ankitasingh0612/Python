# #first create a class 
# class student:#class
#     name="ankita"
#     course="btech"
#  #and then create an object   
# s1=student()#object
# print(s1)
# print(s1.name)
# print(s1.course)



# class cars:
#     color="red"
#     model="marcedes"
#     style="nice"
    
# car1=cars()
# print(car1.model)
# print(car1.color)
# print(car1.style)


#constructor(basically it is init function.it executed when object creation)

#parameterized constructor(self k alawa bhi aur parameter hote h)
# class student:
#     def __init__(self,name,marks):#constructor
#        self.name=name
#        self.marks=marks
#        print("adding new student in database")
       
# s1=student("karan",97) #object
# print(s1.name,s1.marks)

# s2=student("aman",99)
# print(s2.name,s2.marks)

##default constructor(only one parameter i.e self)
#class student:
   #def __init__(self):
   #pass

# #example

# class cars:
#     def __init__(self,carname,color):
#         self.carname=carname
#         self.color=color
#         print("adding new car in database")
        
# car1=cars("aatika","white")
# print(car1.carname,car1.color)
# car2=cars("marcedes","blue")
# print(car2.carname,car2.color)


#class nd instance attributes
 
# class student:
#     college_name="abc college"   # jo cheez common hoti h unke liye class attribute banate h aur 1 he single memory m store karate h
#     name="anonomous"
#     def __init__(self,name):  # ayesha data  jo har ek data k liye alag hota h to uske liye hm self define krte h aur sbko alag alag memory m store krte h 
#       self.name=name
#       print("adding new student")
      
# s1=student("arjun")
# print(s1.name)
# print(s1.college_name)
# print(s1.name)  #obj attr > class attr so that arjun will be printed
         
         
         
#Methods(it is a function that belongs to objects) jo function class k ander likhe jate h unko hm method khte h

# class student:
#     def __init__(self,name):
#         self.name=name
        
#     def welcome(self): #method
#         print("welcome student",self.name)
        
# s1=student("karan")
# s1.welcome()


#static methnod(method that do not use self parameter and work at class level)

# class student:
#     def __init__(self,name):#constructor
#         self.name=name
        
#     def hello(self):#method
#         print("hello",self.name)
#     @staticmethod #decorator(ek ayesha function jo i/p m function leta h aur o/p m bhi function he deta h)  
#     def college():
#         print("itm")
        
# s1=student("ankit")
# s1.hello()
# s1.college()


#Abstraction(hiding the implemntation details 0f a class and showing  only the essential features to the user)

# class car:
#     def __init__(self):
#         self.acc=False
#         self.clutch=False
#         self.brk=False
    
#     def start(self):
#         self.acc=True  #hiiding the implementation details in class
#         self.clutch=True
#         print("car started....")
        
# car1=car()
# car1.start()

#Encapsulation (wrapping data and functions into a single unit(object))

class student:
    def __init__(self):
        self._marks=80
        
    def get_marks(self):
        return self._marks
    
s=student()
print(s.get_marks())        