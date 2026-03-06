#Priyanshu Pabari 590022242

N = int(input("Enter number of students: "))

scores = list(map(int, input("Enter scores separated by space: ").split()))

unique_scores = list(set(scores))

unique_scores.sort(reverse=True)

print("Runner-up score is:", unique_scores[1])