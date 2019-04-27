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

for _ in range(int(input())):
    n, m = map(int, input().split())

    real_m = m//2
    real_m = real_m*2
    mul_value = []

    result = 0

    numerator = 0
    denomi = 1

    for i in reversed(range(m+1)):
        denomi *= (n + i)
        mul_value.append(denomi)

    for i in range(m+1):
        if i %2 == 1:
            continue
        temp =0
        temp_num = 1
        while temp < i:
            temp_num *= (m-temp)
            temp += 1
        temp_num *= n
        numerator += temp_num * (denomi/mul_value[i]) 
    
    common = gcd(denomi, numerator)

    print("{}/{}".format(int(numerator/common), int(denomi/common)))