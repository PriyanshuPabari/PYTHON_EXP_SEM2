#590022242 Priyanshu B1

file = open("city.txt", "r")
lines = file.readlines()
file.close()

print("1. Details of all cities:")
for line in lines:
    print(line.strip())

print("\n2. Cities with population more than 10 lakhs:")
for line in lines:
    data = line.split()
    city = data[0]
    population = float(data[1])
    
    if population > 10:
        print(city)

total_area = 0
for line in lines:
    data = line.split()
    area = float(data[2])
    total_area += area

print("\n3. Sum of areas of all cities:", total_area)