first = True
for _ in range(int(input())):
    if first:
        first= False
        prev_R,prev_G,prev_B = map(int,input().split())
        continue
    R,G,B = map(int,input().split())
    temp_R = R + min(prev_G,prev_B)
    temp_G = G + min(prev_R,prev_B)
    temp_B = B + min(prev_R,prev_G)
    prev_R,prev_G,prev_B = temp_R,temp_G,temp_B
print(min(prev_R,prev_G,prev_B))