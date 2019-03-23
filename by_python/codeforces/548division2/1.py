"""
Q # 1
"""
n = int(input())

test_str = input()
result = 0

for i in range(n):
    if int(test_str[i])%2 == 0: # when it is even
        result = result+i+1

print(result)
