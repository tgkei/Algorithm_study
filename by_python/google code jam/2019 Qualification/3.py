

for C in range(int(input())):
    result =[]
    input()
    i = 1
    #L = list(map(int, input().split()))
    L = list(input().split())
    prime_num1 = 0
    while True:
        i+=1
        temp = int(L[0])
        if temp % i ==0:
            prime_num1= i
            break
    result.append(prime_num1)
    for l in L:
        prime_num1 = int(l)//prime_num1
        result.append(prime_num1)
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
    ans =[]
    for res in result:
        ans.append(dic[res])
    
    print("Case #{}: {}".format(C+1, ''.join(ans)))