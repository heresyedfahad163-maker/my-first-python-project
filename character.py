'''str1="fahad"
str2="shah"
str3="study"
str4="apna"
str5="college"

len1=len(str1)
len2=len(str2)
len3=len(str3)
len4=len(str4)
len5=len(str5)
  
final_str=len1+len2+len3+len4+len5
print(final_str)

str1="shah"
str2="syed"
str3=len(str1+" "+str2)
print(str3)

str="syedfahadshah"
print(str[1:4])
print(str[0:9])
print(str[2:10])
print(str[0:len(str)])
print(len(str))
print(str[:12])
print(str[-12:-1])

 
print("HI") 

light="pink" 

if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("wait")
elif(light=="green"):
    print("go")
else:
    print("run")
 

marks=int(input("Enter your number :"))

if(marks>= 90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
elif(marks>=60 and marks<70):
    grade="D"
elif(marks>50 and marks>60):
    grade="E"
else:
    grade="F"

print("Grade of the student ->",grade)
  

age=95

#nesting
if(age>34):
    if(age>91):
        print("you can drive")
    else:
        print("you can not")
else:
    print("you can not drive")


num=int(input("Enter a number:"))


if(num%2==0):
    print("Even")
else:
    print("Odd")

list=[8,2,4,6,]
list.insert(0,3)
print(list)

list=[1,3,5,7,9]
list.remove(3)
print(list)

list=[1,3,5,7,9]
list.pop(3)
print(list)
 
movies=[]
mov=input("Enter 1st movie:")
movies.append(mov)
mov=input("Enter 2nd movie:")
movies.append(mov)
mov=input("Enter 3rd movie:")
movies.append(mov)


print(movies)

list1=[ "racecar"]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrome:")
else:
    print("not palindrome")


grade=["A","B","A","C","A","D","B"]
print(grade.count("B"))
'''

list=[0,1,2,3,4,5]
list.remove(2)
print(list)



