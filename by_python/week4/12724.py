N = int(input())

for i in range(N):
    result = 0
    input()
    str1 = input().split()
    str2 = input().split()
    int1=[]
    int2=[]
    for str_to_int1, str_to_int2 in zip(str1, str2):
        int1.append(int(str_to_int1))
        int2.append(int(str_to_int2))
    int1.sort()
    int2.sort(reverse=True)

    for k,j in zip(int1, int2):
        result += k*j

    print("Case #{}: {}".format(i+1,result))