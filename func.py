#1.addition funtion
print("ADDITION FUNCTION")
def addition():
    num1=int(input("enter first number = "))
    num2=int(input("enter second number = "))
    print("sum = ",num1+num2)
addition()
print("---------------")
#2.even or odd function
print("EVEN OR ODD FUNTION")
def even_odd():
    num=int(input("enter your number = "))
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
even_odd()
print("--------------------")
#3.largest number function
print("LARGEST NUMBER FUNCTION")
def largest():
    num1=int(input("enter first number = "))
    num2=int(input("enter second number = "))
    if num1>num2:
        print("first number is largest")
    else:
        print("second number is largest")
largest()
print("--------------------")
#4.square funtion
print("SQUARE FUNCTION")
def square():
    num=int(input("enter number = "))
    return num*num
result=square()
print("square = ",result)
print("----------------")
#5.positive,negative or zero function
print("POSITIVE,NEGATIVE OR ZERO FUNCTION")
def check_number():
    num=int(input("enter number = "))
    if num>0:
        print("number is positive")
    elif num<0:
        print("number is negative")
    else:
        print("number is zero")
check_number()