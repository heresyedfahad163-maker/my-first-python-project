for i in range(1,11):
    if i==8:
        break
    print(i)


'''for i in range(1,11):
    if i==5:
        continue
    print(i)'''
while True:
    password = input("Enter password:")
    if password=="python123":
        print("Correct password!")
        break
    else:
        print("Wrong password, try")
        