import sys
sys.setrecursionlimit(111111)

inf = sys.stdin 

T = inf.readline()

def find_smallest(n):
    temp = n
    l = 0
    r = len(n)-1
    arr = [0] * len(n)
    while l < r and temp[l] == temp[r]:
        arr[l] = arr[r] = temp[l]
        l+=1
        r-=1
    if l == r:
        arr[l] =temp[l]
        return int("".join(arr))
    diff = temp[l:r+1]

    if not minimum:
        t = [0] *(r-l+1)
        

    return find_smallest(n[l:r+1])

for t in range(0, int(T)):
    
    Answer=0
    n = int(input())
    li = []

    print('Case #%d' %(int(t)+1))    
    if(n < 10):
        print(1,n)
    else:
        while(n != 0 and len(li) < 4):
            ans = find_smallest(str(n))
            li.append(ans)
            n -= ans
            
        if(len(li) == 4):
            print(0)
inf.close()

"""https://www.codeground.org/practice/practiceProblemViewNew"""

"""import sys

inf = sys.stdin 

T = inf.readline()

for t in range(0, int(T)):
    compare=[]
    sum_1 = {}
    done = False

    n = int(input())

    for i in range(1,10):
        compare.append(i)
    for i in range(1,10):
        compare.append(i*10+i)
    for i in range(1,10):
        for j in range(10):
            compare.append(i*100+j*10+i)
    for i in range(1,10):
        for j in range(1,10):
            compare.append(i*1000+j*100+j*10+i)

    if n in compare:
        print("Case #{}".format(t+1))
        print(1,n)
        done = True
    if done:
        continue

    for comp in compare:
        for comp2 in compare:
            if comp + comp2 == n:
                print("Case #{}".format(t+1))
                print(2,end =" ")
                
                ans = [comp, comp2]
                ans.sort(reverse=True)
                print(*ans)
                done = True
                break
            sum_1[comp+comp2] =(comp,comp2)
        if done: break
    
    if done: continue            

    for comp in compare:
        for key,value in sum_1.items():
            if comp+key == n:
                print("Case #{}".format(t+1))
                ans = []
                ans.append(comp)
                ans.append(value[0])
                ans.append(value[1])
                ans.sort(reverse=True)
                print(3,end=" ")
                print(*ans)
                done = True
                break
        if done: break
    if not done:
        print(0)
inf.close()"""