def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multyply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def avg(num1,num2):
    return (num1/num2)/2

print("select the operation u want to perform \n"\
      "1.addition\n"\
        "2.substraction\n"\
            "3.division\n"\
              "4.multiplication\n"\
                "5.Avg\n")

select=int(input("select operation  from 1,2,3,4,5:"))

num1= int(input("enter the num1: "))
num2= int(input("enter the num2 :"))

if select==1:
    print( num1,"+", num2,"=", add(num1 ,num2))
elif select==2:
     print( num1,"-", num2,"=", sub(num1 ,num2))
elif select==3:
     print( num1,"/", num2,"=", divide(num1,num2))
elif select==4:
     print( num1,"-", num2,"=", multyply(num1,num2))
elif select==5:
     print(" (",num1, "+ ", num2,")", "/", "2","= ", avg(num1,num2))
     
else:
    print("invalid opearations...")