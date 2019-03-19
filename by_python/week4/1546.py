N = int(input())

scores = input().split()

grades = []

avg = 0
for score in scores:
    grades.append(int(score))
    avg += int(score)

max_score=max(grades)

avg = avg/max_score*100

print(avg/N)