'''fruits=["Apple","Banana","PineApple","Peach","Pear"]
fruits[1]="Strawberry"
print(fruits)
print(len(fruits))
fruits.remove[5]'''

'''import random
colors = ['red', 'blue', 'green']
print(random.choice(colors))  # Picks one color randomly'''


'''import calendar
yy=2026
mm=12
print(calendar.month(yy, mm))'''

'''import calendar
yy = 2026 # year
mm = 8   # month
 
# display the calendar
print(calendar.month(yy, mm))'''

balance= 1000000
withdraw_amount=int(input("Enter amount for withdraw..."))

if  500<=withdraw_amount<balance:
    print("Successfully withdraw!")
    print("Thanks for using this ATM.")
elif balance==withdraw_amount:
    print("Your account will be empty and expired!")
elif withdraw_amount<500:
    print("Cannot be Transaction!")
else:
    print("Invalid Amount!")


'''a=8
b=2
if a % b==0:
    print("Divisible")
else:
    if a>b:
        print("Greater")
    else:
        print("Smaller")'''










