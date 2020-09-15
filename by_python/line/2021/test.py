def test(a):
    return 1 if a == 'a' else 0


a = "abcdef"

print(list(map(test, a)))

print(list(map(lambda x: 1 if x == 'a' else 0, a)))
