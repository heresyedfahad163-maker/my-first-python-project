'''n=5
for i in range(n):
    for j in range(i+1):
        print(chr(97+j),end="   ")
        print(chr(65+j),end="   ")
    print()
'''

'''n=26
for i in range(n):
    print(i+1,chr(65+i))
''' 
'''n=5
words=["Python","C++","Java","Javascript","c#"]
for i in range(n):
    print(words[i] ,":",i+1)'''

#List
'''a=["Ali","Irfa","Ayesha","Ahmad"]
a[2]="Laraib"  # change
a.append("Amjad")
a.remove("Ali")
print(a)'''

'''a=["Ali","Irfa","Ayesha","Ahmad"]
for a in a:
    print(a)'''

'''num=[10,12,13,14]
large=max(num)
print("largest:",large)
small=min(num)
print("Smaller:",small)'''

'''list=[]
nums=input("Enter list:")
nums_list = nums.split(",")
list = nums_list
print(list)'''

#practice question 1:

list=[10,15,20,25,30]
average=sum(list)/ len(list)
print("Average:", average)

#practice question 2:

list=[5,4,3,2,1]
list.reverse()
print(list)

#practice question 3:

list=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for num in list:
    if num%2==0:
        even_count +=1
    else:
        odd_count +=1
print("Even number:",even_count)
print("Odd number:",odd_count)

#practice question 4:

duplicate_list=[1,2,2,3,4,5,1,4,2]
unique_list=set(duplicate_list)
print(unique_list)

#practice question 5:

list=[1,5,9,66,7]
list.sort()
second_largest = list[-2]
print(second_largest)



duplicate_list=[1,2,2,3,4,5,1,4,2]
print(duplicate_list)