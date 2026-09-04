a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))

if(a>=b and a>=c):
    print("first number is greater:",a)
elif(b>=c):
    print("second number is greater:",b)
else:
    print("third number is greater:",c)
