'''import math
num=float(input("Enter a number:"))

print("Square:",math.pow(num,2))
print("Sqrt:",math.sqrt(num))
print("Value of PI:",math.pi)
print("Floor:",math.floor(num))
print("Ceil:",math.ceil(num))
'''
 
from countryinfo import CountryInfo
country= CountryInfo(input("Enter Country Name:"))
print("Capital:", country.capital())
print("Population:", country.population())
print("Area (in square kilometers):", country.area())
print("Region:", country.region())
print("Subregion:", country.subregion())
print("Demonym:", country.demonym())
print("Currency:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())



'''data = {
    "A":1,
    "B":2,
    "C":3,
}

del data["B"]
print(data)'''

'''student=[
    {"Name":"Fahad", "ROll no": 23202,"Subject": "python", "CGPA":3.14},
    {"Name":"Sohaib", "ROll no": 23203,"Subject":  "C++"  , "CGPA":3.20},
    {"Name":"Ali",    "ROll no": 23204,"Subject":  "Java"  , "CGPA":3.11},
    {"Name":"Saad",   "ROll no": 23205,"Subject":  "C#"  , "CGPA":2.90},
    {"Name":"Hamza",  "ROll no": 23206,"Subject":  "HTML"  , "CGPA":3.3},
]
print(student[0])
print(student[1]["CGPA"])
print(student[2]["ROll no"])
print(student[3]["Name"])
print(student[4]["Subject"])
print(len("keys"))
print(len("values")) 
'''