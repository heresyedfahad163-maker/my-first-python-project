'''import calculator
number1=input("Enter 1st number:")
number2=input("Enter 2nd number:")
print(number1,number2) 


import random
num=random.randint(1,10)
print("Random number:",num)

import random
name=["sara","fahad","ali","zain","zohaib"]
Anyone=random.choice(name)
print(Anyone)

import random

dice=random.randint(1,6)
print("DICE:",dice)
if dice==1:
    print("move one step....")
elif dice==2:
    print("move two step....")
elif dice==3:
    print("move three step....")
elif dice==4:
    print("move four step....")
elif dice==5:
    print("move five step....")
else:
    print("Wooohooo, you win......")

import random
import string

letters= string.ascii_letters+string.digits
password="".join(random.choice(letters) for i in range(8))
print("Password:",password)

import random

cards=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(cards)
print("Shuffle:",cards)

import random

questions={
      "What is the capital of Pakistan?": "Islamabad",
      "2+2":"4",
      "who made python?": "Guido",
}
q, ans= random.choice(list(questions.items()))
print("Questions:",q)

import random 
num= random.uniform(10,20)
print("Random decimal:",num)'''

'''import random
users=[f"user_{i}" for i in range(1,1001)]
test_users= random.sample(users,1)
print("For test:",test_users)'''

'''employes=["Sana","Maham","Uswa","Iqra","Ali","Shahzaib","Azaan","Saad"]
sallary=200000
bonus=50000
business_profit="85%"
 
if  business_profit<="85%":
    print("Bonus:",employes,sallary+bonus)
else:
    print("no bonus")'''


# ===== Student Management System =====

# 1. dict: سارے students کا ڈیٹا
students = {
    101: {"name": "Ali", "marks": [85.5, 90.0, 78.5], "is_pass": True},
    102: {"name": "Sara", "marks": [92.0, 88.5, 95.0], "is_pass": True},
    103: {"name": "Ahmed", "marks": [45.0, 50.5, 39.0], "is_pass": False}
}

# 2. set: سب subjects کے نام - duplicate نہیں ہوں گے
subjects = {"Math", "Science", "English"}

# 3. range: roll numbers generate کرنے کے لیے
print("Total Students:", len(students))
for roll in range(101, 104): # 101 سے 103 تک
    print("Checking Roll:", roll)

# 4. list + float + int: ہر student کا average نکالنا
print("\n===== Result Card =====")
for roll_no, data in students.items(): # dict + int
    name = data["name"] # string
    marks_list = data["marks"] # list of float

    total = sum(marks_list) # float ka sum
    average = total / len(marks_list) # float division
    average = round(average, 2) # 2 decimal tak

    # 5. bool: pass ya fail
    status = "Pass" if data["is_pass"] else "Fail"

    print(f"Roll: {roll_no} | Name: {name} | Avg: {average} | Status: {status}")

# 6. set operation: کون سے subjects سب کے لیے common ہیں
print("\nSubjects Offered:", subjects)

# 7. Unique feature: Topper نکالنا
topper = max(students.items(), key=lambda x: sum(x[1]["marks"]))
print(f"\nTopper: {topper[1]['name']} with {sum(topper[1]['marks'])} marks")