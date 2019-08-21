from math import inf

nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

x = len(nums1)
y = len(nums2)
if y>x:
    nums1, nums2, x, y = nums2, nums1, y, x
is_odd = (x+y)%2
low = 0
high = x
total_len = (x+y+1)//2
while low <= high:
    x_partition = (low+high)//2
    y_partition = total_len - x_partition
    
    x_left = nums1[x_partition-1] if x_partition else -inf
    x_right = nums1[x_partition] if x_partition != x else inf
    
    y_left = nums2[y_partition-1] if y_partition else -inf
    y_right = nums2[y_partition] if y_partition != y else inf
    
    if x_left <= y_right and y_left <= x_right:
        if is_odd:
            print(float(max(x_left,y_left)))
        else:
            print(float((max(x_left,y_left)+min(x_right,y_right))/2))
    if x_left > y_right:
        high = x_partition - 1
    else:
        low = x_partition+1