#PRIYANSHU PABARI 590022242

# Student details
name = input("Enter student name: ")
roll = input("Enter roll number: ")
sapid = input("Enter SAP ID: ")
sem = input("Enter semester: ")
course = input("Enter course: ")
# Marks input
pds = int(input("Enter PDS marks: "))
python = int(input("Enter Python marks: "))
chem = int(input("Enter Chemistry marks: "))
eng = int(input("Enter English marks: "))
phy = int(input("Enter Physics marks: "))
# Calculation
total = pds + python + chem + eng + phy
percentage = (total / 500) * 100
cgpa = percentage / 10
 # Grade determination
if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"
# Output
print("\n----- Grade Sheet -----")
print("Name:", name)
print("Roll Number:", roll, "\tSAPID:", sapid)
print("Sem:", sem, "\t\tCourse:", course)
print("\nSubject\t\tMarks")
print("PDS\t\t", pds)
print("Python\t\t", python)
print("Chemistry\t", chem)
print("English\t\t", eng)
print("Physics\t\t", phy)
print("\nPercentage:", round(percentage, 2), "%")
print("CGPA:", round(cgpa, 1))
print("Grade:", grade)