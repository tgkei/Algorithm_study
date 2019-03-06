"""
숫자의 총 수 : n (4이상, 10 이하)
뽑는 수 : k (2이상 4 이하)
각 숫자는 1이상 99이하
"""

from itertools import permutations

nums = []
picked = []
result = []

##================================
## 재귀 함수 선언
##================================

def choose (myList, to_go):
    global picked
    global result

    if to_go ==0:
        # 끝 여기서 result 넣어줘
        for num in myList:  # 남아있는 모든 list의 값들을 순차적으로 1의 자리에 넣어준다
            picked.append(num)
            res_num = 0
            two_digit = 0 ## 2의자리까지 가능하니깐
            for i, j in enumerate(reversed(picked)):
                check = j
                if two_digit != 0: ## 그 전 숫자가 2의 자리일 경우 씨바 두자리 수 두개일 경우 생각해줘야 됨
                    j = j * (10**two_digit)
                if check >= 10:     
                    two_digit += 1
                res_num += j*(10**i)
            result.append(res_num)
            picked.pop()
        return

    for i, num in enumerate(myList):
        picked.append(num)
        del myList[i]
        choose(myList, to_go-1)
        picked.pop()
        myList.insert(i,num)

##================================================
## main part
##================================================

n = int(input())
k = int(input())

for _ in range(n):
    nums.append(int(input()))

choose(nums, k-1)

answer = set(result)

print(len(answer))
