# # input function in python
# # a=input("enter the number")
# # print(a) 



# # input function in python
# # name=input("enter the name")
# # print(f"welcome {name} to the python tutorial")

# name1 = input("Enter the student name: ")
# marks1 = int(input("Enter the student marks1 out of(100): "))

# name2 = input("Enter the student name: ")
# marks2 = int(input("Enter the student marks2 out of (100): "))

# name3 = input("Enter the student name: ")
# marks3 = int(input("Enter the student marks3 out of (100): "))
# total_marks= 100
# percentage1= (marks1/total_marks)*100
# print(percentage1)
# print(f"{name1} obtained {marks1} with percentage {percentage1}")

# Input for student 1
# name = input("Enter the student name: ")
# marathi_marks1 = int(input("Enter the student marks1 (out of 100): "))
# hindi_marks2 = int(input("Enter the student marks2 (out of 100): "))
# history_marks3 = int(input("Enter the student marks3 (out of 100): "))

# # Calculate and display percentage for each student
# percentage1 = ((int(marathi_marks1)+int(hindi_marks2)+int(history_marks3))/300) * 100
# print(percentage1)

# print(f"the result of {name} is {percentage1}%")

##operators :
# 1 arithmetic 
# a=5
# b=6
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)

# 2 comparision opearator
# a=5
# b=6
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)

# 3 assignment operator
# a=5

# 4 logical opearator

# a=54
# b=10
# print(a>10 and b>30)
# print(a==54 and b==10)
# print(a==54 or b<10)


#conditiona statement in python
# a=18
# if a<20:
#     print(" u are adult")

# if-else
# a=29
# if a>18:
#     print("u are adult")
# else:
#     print("u are not adult")

# elif statement

# marks=int(input("enter yor marks-10:"))
# if marks >=90:
#     print("grade is :A+")
# elif marks>=80:
#     print("grade is A")
# elif marks>=70:
#     print("grade is B")
# else:
#     print("grade is C")

#nested if else
# num=int(input("enter a number:"))
# if num>0:
#     if num%2==0:
#         print("positive or even")
#     else:
#         print("no is positivee or odd")
# else:
#     print("not  positve or odd and even")

#conditional ecpression(ternary opearator)

# age=26
# status="major" if age>=18 else "major"
# print(status)

# year=int(input("Enter the year:"))
# if year%4==0:
#     print("it's leap year")
# else:
#     print("its not")

#q1
# predefine_username= 'vishakha'
# predefine_password = 'vish@14'

# username= input("enter the username: ")
# password= input("enter the password: ")

# if predefine_username==username:
#     if predefine_password==password:
#         print("login successfuly ")
#     else:
#         print("incorrect password ")
# else:
#     print("invalis username!")



#function
# def greeting():
#     print("hello.... good morning")
# greeting()

# add two numbrs
# def addd2_num( a,b,c):
#     d=a+b+c
#     print("the sum of c is:",d)
# addd2_num(5,6,7)
# addd2_num(a=56,b=78,c=98)

# return statement
# def add3_num(a,b,c):
#     return a+b+c
# sum =add3_num(2,4,65)
# print(sum)

#covrt celsius to fahreheit celcius*9/5+32
# def celsius_fahreheit(celsius):
#     temp1=(celsius *9/5)+32
#     print(temp1)
# celsius_fahreheit(25)    

#argument in function
#requred argu /single/multiple
# def greetings(name):
#     print("hello ", name,"!")

# greetings("vish")

#Default argument/// 

# def intro( name="vish"):
#     print("hello my name is ",name)
# intro()

#keyword argmet//named argument

# def devide(a,b):
#     return a/b
# result=devide(b=45,a=8) #specifiy values using keyword
# print(result)

#arbitrary positional argument (*args)
#u dont know how many argument u want to perform specofic task then we used *args
#we store only in tuple

# def add_numbbers(*args):
#     return sum(args)
# res= add_numbbers(2,3,4,5,6)
# print(res)
#arbitrary keyword argument *kwargs

# def print_detail(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# print_detail(name="vish", age=20, city="pune")


#loops 
# while loop
# x=1
# while x<=10:
#     print(x)
#     x +=1

#for loop

# sql="vishakha"
# for x in sql:
#     print(x)


# for x in range(1,11,2): #start,stop,step
#     print(x)


#loop control statement
# pass,break,continue
 
#pass function is do  nothinng
# for i in range(5):
#  pass
 
# count=5
# while count>0:
#   if count==3:
#      pass
# else:
#  print(count)
#  count -=1

#pass statement is used as placeholder(it does nothing)for the future code and run entie code without cousing any syntax error

# for i in range(5,10):
#     if i==4:
#         pass
#     print(i)


#break statement: terminate the loop entirely 
# for i in range(3,5):
#     if i==4:
#         break
#     print(i)

#continue statement: skip the current iteration an move to the next one
# for i in range(10):
#     if i==4:
#         continue
#     print(i)



#nested loop :  loop inside another loop

# outer loop:
      #inner_loop:
        #block of code
# for i in range(3):
#     print("outer loop iteration",i)
#     for j in range(1,4):
#      print(j)

# i=1
# while i<4:
#     for j in range(1,4):
#         print(j)
#         i=i+1

for num in range (2,10):
    for i in range(2,num):
        if num %i ==0:
            break
        else:
            print(num)
