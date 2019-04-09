str1 = input()
str2 = input()

check = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

i, j = 1, 1

for first in str1:
    for second in str2:
        if first == second:
            check[i][j] = check[i-1][j-1]+1
        else:
            check[i][j] = max(check[i-1][j],check[i][j-1])
        j += 1
    i += 1
    j=1

print(check[-1][-1])