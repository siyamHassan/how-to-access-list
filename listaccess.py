country = ["usa","canada","italy","bangladesh","china"]
# here element access
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])
# for in loop
for a in country:
    print(a)

# list method
country.append("England")
print(country)
country.remove("England")
print(country)
country.pop(0)
print(country)
country.insert(2,"Africa")
print(country)
how_many = country.count("china")
print(how_many)
