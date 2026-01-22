#Priyanshu Pabari 590022242
values = [0, 1]

print("A B | A&B A|B A^B")
print("-------------------")

for A in values:
    for B in values:
        print(A, B, "|", A & B, " ", A | B, " ", A ^ B)