x= "calc1"
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
print("chose operator: +,-,*,/,**,%")
operator=input("enter operator:")

if operator=="+":
    result1=num1+num2
    print(result1)
elif operator=="-":
    result1=num1-num2
    print(result1)
elif operator=="*":
    result1=num1*num2
    print(result1)
elif operator=="/":
    if num2!=0:
        result1=num1/num2
        print(result1)
    else:
        print("Error:no can be divide by zero!")
elif operator=="**":
    result1=num1**num2
    print(result1)
elif operator=="%":
    result1=num1%num2
    print(result1)
else:
    print("Wrong operator:")
    result1=0
print("calc1 result:", result1)


y="calc2"
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=input("Enter an operator:")

if c=='+':
    result2=a+b
    print(result2)
elif c=='-':
     result2=a-b
     print(result2)
elif c=='*':
    result2=a*b
    print(result2)
elif c=='/':
    result2=a/b
    print(result2)
else:
    print("something went wrong:")
    result2=0
print("calc2 result:", result2)
operator=(input("Enter an operator:"))


if operator=='+':
    result3=result1+result2
    print(result3)
elif operator=='-':
     result3=result1-result2
     print(result3)
elif operator=='*':
    result3=result1*result2
    print(result3)
elif operator=='/':
    result3=result1/result2
    print(result3)
else:
    print("something went wrong:")
