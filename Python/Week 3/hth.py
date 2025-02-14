grades = input("nomarat ra vared konid:")
numbers = list(grades)


total = 0
count = 0

for grade in numbers:
    total += grade
    count += 1

average = total / count

print(f"The average grade is: {average}") # Output: The average grade is: 86.6