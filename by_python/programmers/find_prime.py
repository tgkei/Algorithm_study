from itertools import permutations


def make_prime(prime, n):
    p = 2
    while (p * p <= 10 ** n):

        if (prime[p] == True):

            for i in range(p * 2, 10**n, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False


def solution(numbers):
    answer = 0
    n = len(numbers)
    is_prime = [True for i in range(10**n)]
    counted = set()

    make_prime(is_prime, n)

    for i in range(1, n+1):
        permute = permutations(numbers, i)
        for each in permute:
            num = int("".join(list(each)))
            if num in counted:
                continue
            answer += is_prime[num]
            counted.add(num)

    return answer


if __name__ == "__main__":
    print(solution("17"))
