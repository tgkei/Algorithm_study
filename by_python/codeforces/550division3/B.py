input()

numbers = list(map(int,input().split()))

even =[]
odd =[]

for number in numbers:
    if number &1:
        odd.append(number)
    else:
        even.append(number)

even_len = len(even)
odd_len = len(odd)

dif = abs(even_len-odd_len)

if dif <= 1:
    print(0)
else:
    dif -=1
    result = 0
    is_even = True if min(even_len,odd_len)==odd_len else False
    if is_even:
        even.sort(reverse = True)
        for _ in range(dif):
            result += even.pop()
    else:
        odd.sort(reverse = True)
        for _ in range(dif):
            result += odd.pop()
    print(result)