"""input()

chest = list(map(int,input().split()))
keys = list(map(int,input().split()))

odd_chest = 0
even_chest = 0
odd_keys = 0
even_keys = 0

for c in chest:
    if c % 2 ==0:
        even_chest+=1
    else:
        odd_chest+=1

for key in keys:
    if key % 2 == 0:
        even_keys +=1
    else:
        odd_keys +=1

result = 0
result += min(odd_chest, even_keys)
result += min(even_chest, odd_keys)

print(result)"""




### 좋은 방법!
"""
Sample Solution
We only need to number of odd and even numbers
Therefore, just make an list that has 'x%2' which will give 0 for even and give 1 for odd number
Sum up list gonna be same as the number of odd
Anything else are same logic
"""
"""R=lambda:map(int,input().split())
n,m=R()
a,b=(sum(x%2 for x in R()) for _ in (0,0))
print(min(a,m-b)+min(n-a,b))"""

m, n = map(int,input().split())

odd_first= [x % 2 for x in map(int,input().split())]
odd_second = [x% 2 for x in map(int,input().split())]

odd_first = sum(odd_first)
odd_second = sum(odd_second)

print(min(odd_first,n-odd_second)+min(m-odd_first,odd_second))