'''fruits=["apple","banana","mango","peach","cherry","plum","melon","strawberry","watermelon"]
idx=0
for val in fruits:
    print(val)
    if(val=="peach"):
        print("index:",idx,"value:",val)
        print(type(fruits))
         
    idx=idx+1

idx=fruits.index("peach")
print("value:",idx)'''

'''str="syedfahadshah"
for char in str:
    if(char=='h'):
        print("h found")
        break
    print(char)
else:
 print('END')'''
'''
nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    if(el==9):
        print('found number=9')
        break
    print(el)
print('end')
 '''
nums=[1,4,9,16,25,36,49,64,81,100,36]
x=36
idx=0
for el in nums:
    if(el==x):
        print("number found at idx",idx)
        break
    idx+=1
