#PRIYANSHU PABARI 590022242

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and distinct")
    print("Root1:", root1)
    print("Root2:", root2)
elif D == 0:
    root = -b / (2*a)
    print("Roots are real and equal")
    print("Root:", root)
else:
    print("Roots are imaginary")