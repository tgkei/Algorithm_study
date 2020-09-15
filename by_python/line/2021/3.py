def solution(n):
    answer = []

    length = len(str(n))
    a1 = 0
    while length > 1:
        left = length//2 + 1 if length % 2 else length//2
        str_n = str(n)
        str_l = str_n[:left]
        str_r = str_n[left:]

        if int(str_r) == 0:
            str_l = str_n[:-1]
            str_r = str_n[-1]
        elif str_r[0] == '0':
            idx1 = len(str_l) - 1
            while str_l[idx1] == '0':
                idx1 -= 1
            l1 = str_l[:idx1+1]
            r1 = str_n[idx1+1:]

            idx2 = 0

            while str_r[idx2] == '0':
                idx2 += 1

            l2 = str_l + str_r[:idx2]
            r2 = str_r[idx2:]
            if max(len(l1), len(r1)) < max(len(l2), len(r2)):
                str_l = l1
                str_r = r1
            else:
                str_l = l2
                str_r = r2

        l_num = int(str_l)
        r_num = int(str_r)

        n = (l_num + r_num)
        length = len(str(n))
        a1 += 1

    answer = [a1, n]

    return answer


if __name__ == "__main__":
    n = 1000
    print(solution(n))
