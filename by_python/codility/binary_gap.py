N = int(input())

bin_num = "{0:b}".format(N)

print(bin_num)

zero_num = 0
max_zero = 0
    
for num in bin_num:
    if num == '1':
        max_zero = max(max_zero,zero_num)
        zero_num = 0
    elif num =='0':
        zero_num+=1

print(max_zero)