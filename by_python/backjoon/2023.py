from math import sqrt

def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def make(n,th=1):
    if th == num:
        if is_prime(n):
            print(n)
        else:
            return False
    else:
        if is_prime(n):
            for i in range(1,10,2):
                temp = n*10 +i
                make(temp,th+1)
        else:
            return False

num = int(input())

for i in [2,3,5,7]:
    make(i)