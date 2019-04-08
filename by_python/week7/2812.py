N, K =map(int,input().split())
nums = input()

target = N-K
stack = []
len_stack = len(stack)
len_remain = len(nums)
remain = []
done = False

for i, num in enumerate(nums):
    len_remain -= 1
    if len_stack != 0:
        while stack and stack[-1] < num:
            stack.pop()
            len_stack -= 1
            if len_remain+ len_stack+1 == target:
                stack.append(num)
                len_stack +=1
                break
        else:
            len_stack+=1
            stack.append(num)
    else:
        stack.append(num)
        len_stack += 1

    # in case of sum of the number of elements in stack and remaining words equals to the target
    if len_remain + len_stack == target:
        if len_remain != 0:
            result = ''.join(stack)+''.join(nums[i+1:])
            done = True
        break

if not done:
    result = ''.join(stack[:target])

print(result)
