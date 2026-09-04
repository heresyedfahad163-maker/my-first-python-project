info = {
    "name" :"Fahad",
    "class": "IT",
    "rollno":23202,
    "subject":["python","c++","javascript"],
    "topics":("loops","string"),
    "cgpa":3.42,
}
print(info["name"])
print(info["subject"])
print(info["topics"])
info["surname"]="shah"

null_dict ={}
null_dict["hobby"]="gardening"
null_dict["professor"]="shradha"
print(null_dict)

student={
    "name":"wali",
    "surname":"shah",
    "subject":{
            "phy": 95, 
            "chem":97,
            "bio":98,
    }
}
print(student.get("name"))
print(student.get("surname"))

marks={}

x=int(input("Enter phy:"))
marks.update({"phy":x})

x=int(input("Enter chem:"))
marks.update({"chem":x})

x=int(input("Enter bio:"))
marks.update({"bio":x})

print(marks)