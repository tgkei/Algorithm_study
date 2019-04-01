for i in range(int(input())):
    result = 0
    d, inst = input().split()
    d = int(d)
    num_s = inst.count('S')
    if num_s > d:
        print("Case #{}: IMPOSSIBLE".format(i+1))
        continue
    for i in range(1, len(inst)+1):
        if inst[-i] == 'C':
            continue
        elif inst[-i] == 'S' and inst[-(i+1)] == 'C':
            temp_1 = inst[:-(i+1)] +'S'+'C'+inst[-(i-1):]
    print("Case #{}: {}".format(i+1,result))