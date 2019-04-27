from math import inf

input()

vocab ={ 'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26}

minimum = inf
s = list(input().lower())

for i in range(len(s)-3):
    cost = 0
    first = abs(vocab[s[i]]-vocab['a'])
    if first >13:
        first = (26-first)
    cost += first
    
    second = abs(vocab[s[i+1]] - vocab['c'])
    if second > 13:
        second = (26-second)
    cost += second
    
    third = abs(vocab[s[i+2]] - vocab['t'])
    if third >13:
        third = (26-third)
    cost+= third
    
    fourth = abs(vocab[s[i+3]] - vocab['g'])
    if fourth >13:
        fourth_1 = (26-fourth)
    cost+= fourth
    
    minimum = min(minimum,cost)

print(minimum)