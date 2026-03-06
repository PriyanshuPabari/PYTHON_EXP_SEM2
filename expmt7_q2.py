#590022242 Priyanshu B1

file = open("numbers.txt", "r")
numbers = file.read().splitlines()
file.close()

numbers = [int(num) for num in numbers]

max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

count = 0
for num in numbers:
    if num > 100:
        count += 1

print("1. Maximum number:", max_number)
print("2. Average of numbers:", average)
print("3. Numbers greater than 100:", count)