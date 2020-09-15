from pprint import pprint
from bisect import bisect, bisect_left


def find_ge(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]


class Tree:
    def __init__(self):
        self.head = dict()

    def create_node(self, conditions):
        tracker = self.head
        for c in conditions[:-1]:
            if c not in tracker:
                tracker[c] = dict()
            tracker = tracker[c]
        score = conditions[-1]
        if "score" not in tracker:
            tracker["score"] = dict()
            tracker["score"][score] = 1
        else:
            if score in tracker["score"]:
                tracker["score"][score] += 1
            else:
                tracker["score"][score] = 1

    def calc(self):
        tracker = self.head

        stack = [tracker]
        while stack:
            cur = stack.pop()
            if "score" in cur:
                # calculate prefix sum
                cur["index"] = []
                prefix_sum = 0
                tmp = sorted(cur["score"].items())
                for k, v in reversed(tmp):
                    prefix_sum += v
                    cur["score"][k] = prefix_sum
                    cur["index"] = [k] + cur["index"]
                continue
            for v in cur.values():
                stack.append(v)

    def search(self, query):
        ret = 0
        tracker = self.head

        stack = [(tracker, query)]
        while stack:
            cur, q = stack.pop()

            if q[0] == '-':
                for v in cur.values():
                    stack.append((v, q[1:]))
            elif "score" in cur:
                idx = find_ge(cur["index"], q[0])

                try:
                    ret += cur["score"][idx]
                except:
                    continue
            else:
                try:
                    stack.append((cur[q[0]], q[1:]))
                except:
                    continue
        return ret

    def show(self):
        pprint(self.head)


def parse_info(info):
    ret = list(info.split(" "))
    ret[-1] = int(ret[-1])
    return ret


def parse_query(query):
    ret = list(query.split(" and "))
    food, score = ret[-1].split(" ")
    ret[-1] = food
    ret.append(int(score))
    return ret


def solution(info, query):
    answer = []

    tree = Tree()

    for each_info in info:
        i = parse_info(each_info)
        tree.create_node(i)
    tree.calc()

    for q in query:
        q = parse_query(q)
        answer.append(tree.search(q))

    return answer


if __name__ == "__main__":
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
    print(solution(info, query))
