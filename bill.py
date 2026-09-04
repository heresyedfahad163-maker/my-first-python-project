'''import math
num=float(input("Enter a number:"))

print("Square:",math.pow(num,2))
print("Sqrt:",math.sqrt(num))
print("Value of PI:",math.pi)
print("Floor:",math.floor(num))
print("Ceil:",math.ceil(num))'''

from  countryinfo import CountryInfo

country = CountryInfo(input("Enter Country Name: "))

print("Capital:", country.capital())
print("Population:", country.population())
print("Area (in square kilometers):", country.area())
print("Region:", country.region())
print("Subregion:", country.subregion())
print("Demonym:", country.demonym())
print("Currency:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())
 