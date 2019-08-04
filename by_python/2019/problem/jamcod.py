"""s = input()
t = sorted(s)
n = int(input())
res = set()
ind = 0
while(len(res)<n):
    for i in range(len(s)):
        if t[ind] == s[i]:
            if i+n+1 <=len(s)+1:
                for j in range(i+1,i+n+1):
                    res.add(s[i:j])
            else:
                for j in range(i+1,len(s)+1):
                    res.add(s[i:j])
    ind+=1
res = sorted(list(res))
print(res[n-1])"""

"""def is_palindrome(s):
    for i, j in zip(range(len(s)//2),range(len(s)-1,0,-1)):
        if s[i] != s[j]:
            return False
    return True

s = input()
res = 0
for i in range(len(s)):
	for j in range(i,len(s)):
		if is_palindrome(s[i:j+1]):
			res = max(res,j+1-i)
print(res)"""

#사은품 교환하기
for _ in range(int(input())):
    n, m = map(int,input().split())
    cur_n = 5
    res = 0
    while cur_n <=12 and n>=cur_n:
        cur_m = 12-cur_n
        if cur_m == 0:
            res += n//12
            break
        if m>=cur_m:
            t=min(n//cur_n,m//cur_m)
            m -= (cur_m * t)
            n -= (cur_n * t)
            res +=t
        cur_n +=1
    print(res)

"""from collections import Counter
def solution(participant, completion):
    answer = ''
    c= Counter(participant)
    for com in completion:
        c[com]-=1
    answer = c.most_common(1)[0][0]
    return answer"""