import sys

def gcd(m,n):
    while True:
        if n > m :
            m, n = n, m
        r = m%n
        if (r ==0):
             return n
        else:
            m = n
            n = r

for C in range(int(input())):
    result =[]
    input()
    L = list(map(int, sys.stdin.readline().split()))
    
    i = 0
    while (L[i]==L[i+1]):
        i+=1

    temp = []
    prime_num = gcd(L[i],L[i+1])
    temp.append(prime_num)
    temp_prime_num = L[i]//prime_num    
    temp.append(temp_prime_num)
    
    for j in reversed(range(i)):
        temp_prime_num = L[j]//temp_prime_num
        temp.append(temp_prime_num)
    while temp:
        result.append(temp.pop())
    
    for l in L[i+1:]:
        prime_num = l//prime_num
        result.append(prime_num)
    L = None

    result2 = set(result)
    result2 = sorted(result2)
    result2 = iter(result2)
    dic ={}
    dic[next(result2)] = 'A'
    dic[next(result2)] = 'B'
    dic[next(result2)] = 'C'
    dic[next(result2)] = 'D'
    dic[next(result2)] = 'E'
    dic[next(result2)] = 'F'
    dic[next(result2)] = 'G'
    dic[next(result2)] = 'H'
    dic[next(result2)] = 'I'
    dic[next(result2)] = 'J'
    dic[next(result2)] = 'K'    
    dic[next(result2)] = 'L'
    dic[next(result2)] = 'M'
    dic[next(result2)] = 'N'
    dic[next(result2)] = 'O'    
    dic[next(result2)] = 'P'
    dic[next(result2)] = 'Q'
    dic[next(result2)] = 'R'
    dic[next(result2)] = 'S'
    dic[next(result2)] = 'T'
    dic[next(result2)] = 'U'
    dic[next(result2)] = 'V'
    dic[next(result2)] = 'W'
    dic[next(result2)] = 'X'
    dic[next(result2)] = 'Y'
    dic[next(result2)] = 'Z'
    result2 =None
    ans =[]
    for res in result:
        ans.append(dic[res])
    
    print("Case #{}: {}".format(C+1, ''.join(ans)))