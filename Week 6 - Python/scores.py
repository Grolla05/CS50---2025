#scores = [72, 73, 33]

#average = sum(scores) / len(scores)
#print(f"Average: {average}")

scores = []

for i in range(3):
    score = int(input("Score: "))
    scores.append(score)

average = sum(scores) / len(scores)

print(f"Average: {average}")
