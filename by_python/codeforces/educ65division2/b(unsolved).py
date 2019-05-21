import sys

nums = [4,8,15,16,23,42]
dic = {}


result = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        dic[nums[i]*nums[j]] = (nums[i],nums[j])

def find(x,y,z):
    print("? {} {}".format(x, y),flush=True)
    num1 = int(input())

    print("? {} {}".format(y, z),flush=True)
    num2 = int(input())

    (a1,a2)=dic[num1]
    (a3,a4)=dic[num2]

    if a1 == a3: return [a2,a3,a4]
    if a2 == a3: return [a1,a2,a4]
    if a1 == a4: return [a2,a1,a3]
    return [a1,a2,a3]

    

result = find(1,2,3) + find(4,5,6)

print("!",*result)