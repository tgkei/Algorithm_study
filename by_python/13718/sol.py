numbers = input()
original = input()
_, M, K, X = numbers.split()
M, K , X =int(M), int(K), int(X)-1

remainder=[]

# K+1 진수로 바꿔주는 부분
while X >= K:
    remainder.append(X%(K)) ## 이때 index가 1 더해져 있음
    X = X//(K) 

remainder.append(X) ## 다 나누고 남은 나머지도 remainder에 넣어줌

if len(remainder) != M:
    for _ in range(M-len(remainder)):
        remainder.append(0)

letter =[]

# 저장한 remainder 리스트에서 값을 하나씩 빼와서 해당 단어를 입력 받고 바꾸기
# 이때 remainder가 먼저 없어지는 경우도 생각해야 함 씨부렐
while remainder:
    #입력 받음
    letters = input()

    #입력 받은 스트링을 list로 바꿈
    for i in range(len(letters)):
        letter.append(letters[i])

    letter.sort()
    
    original = original.replace('#',letter[remainder.pop()],1)
    letter=[]

print(original)