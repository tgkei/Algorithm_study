from itertools import combinations


def solution(orders, course):
    answer = []
    #ans_set = set()

    for num in course:
        tmp = dict()
        most_str = set()
        most_num = 2
        for order in orders:
            order = sorted(list(order))
            if len(order) < num:
                continue
            combis = combinations(order, num)
            for combi in combis:
                comb_lst = sorted(list(combi))
                str_combi = ''.join(comb_lst)
                if str_combi in tmp:
                    tmp[str_combi] += 1
                else:
                    tmp[str_combi] = 1

                if most_num == tmp[str_combi]:
                    most_str.add(str_combi)
                    most_num = tmp[str_combi]
                elif most_num < tmp[str_combi]:
                    most_num = tmp[str_combi]
                    most_str = set()
                    most_str.add(str_combi)
        answer += most_str

    return sorted(answer)


if __name__ == "__main__":
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2, 3, 5]
    print(solution(orders, course))
