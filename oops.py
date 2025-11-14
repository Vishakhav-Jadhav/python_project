#using oops
# class
#self: refference 

# class Student:
#   def __init__(self,name,grade ,percentage ,team):
#     self.name=name
#     self.grade=grade
   #  self.percentage=percentage
#     def detail(self):
#       print(f"{self.name}is in class {self.grade} with percentage({percentage}%")

# #object 
# Studen1=Student('vish','A',56%)
# print(Studen1.name,  Studen1.grade ,student1.percentage)
#Student=student ("xyz",24,78%)
# print(Student.name, Student.grade,student.percentage)


# class teacher:
#     def __init__(self , name,age):
#         self.name = name 
#         self.age = age


#     def teache_detail(self):
#        print(f"student name is {self.name} age is {self.age}")

# #object

# t1=teacher("vish",21)           
# t1.teache_detail()

# t1.age= 5
# del t1.age



# #features of features
# 1 abstraction :: hiding unneccesary detail form user throught method
# #2 
# class Student:
#   def __init__(self,name,grade ,percentage ,team):
#     self.name=name
#     self.grade=grade
#     self.percentage=percentage
#     def sudent_detail  (self):
#       print(f"{self.name}is in class {self.grade} with percentage({percentage+2}%")


# #object 
# Studen1=Student('vish','A',89)
# print(Studen1.name,  Studen1.grade )
# Student2=Student("bhb",'B',67)
# print(Student2.name,Student2.age)
# print(sudent_detail)


#inheritance: allow a one class to resue the properties and methods to onother class
# 1 eg
# class Student:
#   def __init__(self,name,grade ,percentage ,team):
#     self.name=name
#     self.grade=grade
#     self.percentage=percentage
#     self.team=team
#     def student_detail(self):
#         print(f"{self.name} is in class {self.grade} with percentage ({self.percentage + 2}%)")
# team1="A"
# team2="B"
# #object 
# Studen1=Student('vish','A',56,team1)
# print(Studen1.name,  Studen1.grade,Studen1.percentage,Studen1.team)
# Student2=Student("bhb",'B',78,team2)
# print(Student2.name,Student2.grade ,Student2.percentage,Student2.team)
# print(student_detail)





#inheritance

# class person:
#     def __init__(self, firstname, lastname):
#         self.firstname=firstname
#         self.lastname=lastname

#     def  print_name(self):
#         print(f"the person name is {self.firstname} and tha last name is {self.lastname}")

# class student(person):
#     def __init__(self, firstname, lastname ,year):
#         super().__init__(firstname, lastname)
#         self.graduationyear=year

#     def welcome(self):
#          print(f"Welcome {self.firstname} {self.lastname} to class of {self.graduationyear}")



# # p1=person("vish","jadhav")
# # print(p1.firstname,p1.lastname)
# # p1.print_name()

# s1=student("vish","jadhav",2025)
# s1.print_name()
# s1.welcome()


#polymorphisam: many form ..method  fucnt operators with same name that can  executed on many different way 
#same method name can behave differetly depending on the that obj calls it

# class animal:
#     def speak(self):
#         print("animal make a sound")

# class Dog (animal):
#     def speak(self):
#       print("bark")

# class  cat(animal):
#     def speak(self):
#         print("meww")

# def animal_sound(animal):
#         animal.speak()

# a= animal()
# b= Dog()
# c=cat()
# animal_sound(a)
# animal_sound(b)
# animal_sound(c)

#polymorphism:

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("drive")

# class Boat:
#     def __init__(self, brand2, model2):
#         self.brand2 = brand2
#         self.model2 = model2

#     def move(self):
#         print("Sail")


# class Plane:
#     def __init__(self, brand3, model3):
#         self.brand3 = brand3
#         self.model3 = model3

#     def move(self):
#         print("Flying")
    
# c1=Car("Ford", "Mustang")
# b1=Boat("Ibiza", "Touring 20")
# p1=Plane("Boeing", "747")

# c1.move()
# b1.move()
# p1.move()

# for i in (c1,b1,p1):
#    i.move()


#Abstraction: abstraction means hiding a internal detail and showing only essential features

# from abc import ABC, abstractmethod

# class  vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class car(vehicle):
#      def start(self):
#         print("starting")

# class Bike(vehicle):
#      def start(self):
#         print("bike started")

# c1=car()
# c1.start()

# b1=Bike()
# b1.start()

# v1=vehicle() //abstrac method can't call
# v1.start()

#encapsulation: buinding method / data in single  unit and protecting from outside interface:

# class BankAccount:
#     def __init__(self, name,balance):
#         self.name=name
#         self._balance=balance //private variable


#     def deposite(self,amount):
#         self._balance+=amount

#     def get_balance(self):
#         print(self._balance)


# ac=BankAccount('vish',400)
# ac.deposite(500)
# print(ac.get_balance())
# print(ac._balance) //throught errors because balance is pribate variable 