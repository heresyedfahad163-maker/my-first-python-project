'''students={
  23201:{"Name":"Fahad","Marks":[98.9,97.9,96.5],"is_Pass":True},
  23202:{"Name":"Dua","Marks":[99.4,98.3,94.8],"is_Pass":True},
  23203:{"Name":"Falak","Marks":[45.5,34.5,20.9],"is_Pass":False},
  23204:{"Name":"Saad","Marks":[87.5,88.5,90.9],"is_Pass":True},
  23205:{"Name":"Asfand","Marks":[76.5,67.5,90.9],"is_Pass":True},
  23206:{"Name":"Zara","Marks":[50.5,24.5,18.9],"is_Pass":False},
}
Subjects={"Biology","Chemistry","Physics"}

print("Total Students:",len(students))
for roll in range(23201,23207):
    print("Checking Roll_no.",roll)

print("\n====RESULT CARD====")
for Roll_no ,data in students.items():
    Name=data["Name"]
    Marks_list=data["Marks"]

total=sum(Marks_list)
average=total/len(Marks_list)
average=round(average,2)

status="Pass" if data["is_Pass"] else "Fail"
print(f"Roll_No{Roll_no} | Name{Name} | Average{average} | Status{status}")

print("\n Subjects Offered:",Subjects)

topper = max(students.items(), key=lambda x: sum(x[1]["Marks"]))
print(f"\nTopper: {topper[1]['Name']} with {sum(topper[1]['Marks'])} Marks")  '''

square=lambda x:x**2
print(square(5))

add=lambda a,b:a+b
print(add(3,2))