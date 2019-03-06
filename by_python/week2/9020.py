##======================================================================
## 에라토스테네스의 체
##======================================================================
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    sieve[0] = False
    sieve[1] = False
    return sieve

##====================================================================
## 데이터 받아오기
##====================================================================
T = int(input())
n=[]
for _ in range(T):
    n.append(int(input()))

prime_number = prime_list(max(n))

##====================================================================
## 파티션 찾기
##====================================================================

for num in n:
    
    part1 = 0
    part2 = 0
    i = 1
    j = num-1
    for _ in range(num//2):
        if prime_number[i] and prime_number[j]:
            part1 = i
            part2 = j
        i+=1
        j-=1
            
    print(part1,part2)