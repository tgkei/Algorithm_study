"""
방법 1 deque 사용 pop하는 경우가 아니면 뒤로 이동시키는 방법
시간 초과 나옴
"""
"""
from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    number = deque()
    result = 0
    for i in range(n):
        number.append(str(i+1))
    # 숫자 다 넣어짐
    i = 0
    number.popleft()
    while len(number) > 2:
        i +=1
        if i != k:
            number.rotate(-1)
        else:
            i = 0
            number.popleft()
    number = list(sorted(number))
    result = ' '.join(number)
    print(result)
"""
"""

방법 2 직접 linked list를 구현했는데 이것도 시간초과 ㅡㅡ

import time

class node:
    def __init__(self, data,prev = None, nex= None):
        self.data = data
        self.next = nex
        self.previous = prev

class linked:
    def __init__(self):
        self.head = None
        self.current = None
        self.len = 0
        self.iter = None
    
    def move_right(self):
        self.iter = self.iter.next
    
    def move_left(self):
        self.iter = self.iter.previous

    def append(self, value):
        if self.len == 0:
            self.current = self.head = node(data = value)
            self.current.next = self.current.previous = self.current
            self.iter = self.head
        else:
            self.current.next = node(data = value, prev = self.current, nex = self.head)
            self.head.previous = self.current.next
            self.current = self.current.next
        self.len +=1    
    
    def getlen(self):
        return self.len

    def delete(self):
        assert (self.len != 0), "no node left"
        self.len -=1
        self.iter.previous.next = self.iter.next
        self.iter.next.previous = self.iter.previous
        a = self.iter
        self.iter = self.iter.next
        if a == self.head:
            self.head = self.head.next
        value = a.data
        del a
        return value
t = 0.0
           
for _ in range(int(input())):
    link = linked()
    result = []
    n, k = map(int, input().split())
    a = time.time()
    for i in range(1,n):
        link.append(str(i+1))
    cnt = 0
    while link.getlen() > 2:
        cnt+=1
        if cnt == k:
            cnt = 0
            link.delete()
        else:
            link.move_right()
    while link.getlen() != 0:
        result.append(link.delete())
    result.sort()
    result = ' '.join(result)
    print(result)

    del link
    b = time.time()
    t += (b-a)
print(t)
"""
"""
방법 3 뒤에서 부터 돌려보자 (이거 popleft가 1일줄 알았는데 아니라 의미 없음 실질적으로 rotate가 문제)
import time
from collections import deque
t = 0.0
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = time.time()
    number = deque()
    result = 0
    for i in range(n,1,-1):
        number.append(str(i))
    # 숫자 다 넣어짐

    i = 0
    while len(number) > 2:
        i +=1
        if i != k:
            number.rotate(1)
        else:
            i = 0
            number.pop()
    number = list(sorted(number))
    result = ' '.join(number)
    print(result)
    b = time.time()
    t+= (b-a)
print(t)"""
