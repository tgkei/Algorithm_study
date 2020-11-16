alphas = "abcdefghijklmnopqrstuvwxyz"


def editDistance(source, target):
    alpha_to_num = dict()
    num_to_alpha = dict()
    N = len(alphas)
    for i in range(N):
        alpha_to_num[alphas[i]] = i
        num_to_alpha[i] = alphas[i]

    target_list = []
    for t in target:
        target_list.append(alpha_to_num[t])

    minimum = int(1e9)
    for additional in range(N):
        tmp_list = []
        for each in source:
            idx = (alpha_to_num[each] + additional) % N
            tmp_list.append(idx)

        weight = 0
        for s, t in zip(tmp_list, target_list):
            if s == t:
                continue
            weight += 1
        if weight < minimum:
            minimum = weight
    return minimum


if __name__ == "__main__":
    source = "abc"
    target = "gzu"

    print(editDistance(source, target))
