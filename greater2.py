a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))

if(a>=b and a>=c and a>=d):
    print("first number is greater:",a)
elif(b>=c and b>=d):
    print("second number is greater:",b)
elif(c>=d):
    print("third number is greater:",c)
else:
    print("fourth number is greater:",d)