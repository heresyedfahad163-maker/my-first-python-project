#tuple
'''a=("ali","saad","ahmad")
print((a)[1])'''

'''student=("ali",31,33301028384, "1152/1200")
print("name:",student[0])
print( "age:",student[1])
print("CNIC:",student[2])
print( "marks:",student[3])'''


nums=(12,13,10,20,15)
total=sum(nums) 
print(nums)
print(total)

nums=(10,12,31,32,54,45,21,7,43)
small=min(nums)
large=max(nums)
print("Small:",small)
print("Large:",large)


student=("ali","sana","talha","zain")
name=input("Enter student:")
if name in student:
    print(name,"found student.....")
else:
    print("not found!")

a=[*{1,2,3},*{4,5,6}]
print(a)

name=[*{'shah'},*{'ali'}]
print(name)
