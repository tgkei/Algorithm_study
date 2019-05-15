def solve(n):
    if n==0:
        return 1
    elif n == -1:
        return 0
    x= n//10
    return max(int(n%10) * solve(x), 9 * solve(x-1))

num = int(input())
print(solve(num))