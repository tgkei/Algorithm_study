from collections import Counter

n, m = map(int,input().split())

answers = []
for _ in range(n):
    answers.append(list(input()))
scores = list(map(int,input().split()))
res = 0
for i in range(m):
    temp = [a[i] for a in answers]
    c = Counter(temp)
    res += (scores[i] * c.most_common(1)[0][1])

print(res)