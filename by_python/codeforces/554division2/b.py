"""
###error when input is 699050
Since it add one after do the xor operation, if last number is 0, after xor operartion, the value will be 1 and plus 1 will result
10

x = int(input())

x = format(x,"b")

pos =[]

i = len(x)
current = x[0]

total = 0
result = ""

for bit in x:
    if i == 1:
        break
    if bit != current:
        current = bit
        pos.append(str(i))
    i -= 1

if len(pos) == 0 and x[-1] == "0":
    print(1)
    print(1)
else:
    total = total + (2* len(pos))
    if x[-1] == "0":
        total -=1
    print(total)
    print(" ".join(pos))
"""
"""
t가 홀수일 때마다 +1을 한다 (실제로는 0부터 시작이라 짝수번 째 때 +1을 한다)
x 에 x길이 만큼의 111111 을 xor 연산하면 맨 앞은 0이되고 그 다음이 0이 될 때까지 다 지워진다.

x = int(input())
ans = []
t = 0
while x != 2 ** x.bit_length() - 1:
    if t % 2:
        x += 1
    else:
        xb = x.bit_length()
        ans.append(xb)
        x ^= 2 ** xb - 1
    t += 1
print(t)
print(*ans)
"""
x = int(input())

answer = 0

ans_array=[]

T = 0

while x != 2**x.bit_length()-1:
    if T % 2 == 0:
        ans_array.append(x.bit_length())
        x ^= (2**x.bit_length()-1)
    else:
        x += 1
    T+=1
print(T)
print(*ans_array)