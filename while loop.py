'''i=10   
while i>=1:
    print(i)
    i-=1

i=1

while i<=10:
    print(i)
    i+=1
n=int(input("Enter number:"))
i=1

while i<=10: 
    print(n**i)
    i+=1
n1=(input("enter a name:"))
n2=(input("enter a name:"))
n3=(input("enter a name:"))
n4=(input("enter a name:"))
n5=(input("enter a name:"))
i=1
while i<=150:
    print(i ,n1,n2,n3,n4,n5)
    i+=1 

nums=(5,10,15,20,34,12,34,16,38,33,34,55,12,12,1,2,12) 
x=55
i=0
while i<len(nums):
    if(nums[i]==x):
       print("found at idx:",i)
    elif(nums[i]==55):
        print("nothing:")
    else:
        print("there is no number:")
    i+=1

list=[4,2,3,1,2]
x=5
i=0
while i<len(list):
    if(list[i]==x):
        print("found at idx",i)
    else:
        print("no value at idx")
    i+=1 

i=1
while i<=7:
     
    if(i%2==0):
        i+=1
        continue
    print(i)     
    i+=1

nums =(12,13,2,2,3,1,43,54,23,65,4,3,2,1,2)
i=0
while i<len(nums):
    if(nums[i]%2==0):
        print("even",nums[1])
i+=1

i=1
while i<=50:
    print(i,"Allied Hospital Faisalabad.")
    i+=1'''

'''n=8
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Sum total:",sum)'''
'''n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("total factorial=",fact)'''

n=1
fact=1
i=5
while i>=n:
    fact*=i
    i-=1
print("total factorial=",fact)