### 방법 1: 존나 귀찮은데 어떤 언어에서도 사용 가능 방법 (파이썬 형식으로 썼음)
a = [1,3,5]
b= [1,2,5,7,8]

intersection = []

for x in a: ## a 배열에 있는 값들 하나 하나 확인
    for y in b: ## b 배열에 있는 값들 하나 하나 확인
        if x == y:
            intersection.append(x) ## union이라는 배열에 x 값 추가 c++에서 vector 쓰면 이 기능 있음

for x in intersection: ## 
    if x in a:
        a.remove(x)

result = a+b

result.sort()

print(result)

### 방법 2: 파이썬이면 가능한 방법
a = {1,3,5}
b = {1,2,5,7,8}

a.union(b)

