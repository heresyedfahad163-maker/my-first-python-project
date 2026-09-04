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
yy = 2012 # year
mm = 12   # month
 
# display the calendar
print(calendar. month(yy, mm))'''


'''students = [] # یہاں data save ہوگا

def add_student():
    name = input("Student Name: ")
    roll = input("Roll No: ")
    students.append({"name": name, "roll": roll})
    print("Student Added!")

def view_students():
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}")

while True:
    print("\n1. Add Student 2. View 3. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break'''



n=5
for i in range(n):
    print("A"*(i+1))