input()
s = input()

n = len(s)
pos = n//2
left = pos
right = pos+1
while s[left] == '0':
    left-=1
while right < n and s[right] == '0':
    right +=1
if left == 0:
    res = int(s[:right])+int(s[right:])
elif right == n:
    res = int(s[:left])+int(s[left:])
else:
    res = min(int(s[:left])+int(s[left:]),int(s[:right])+int(s[right:]))
print(res)