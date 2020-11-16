from itertools import combinations
from pprint import pprint

num_of_attri = int(input())
support_thres = float(input())
N = int(input())

db = []
attributes = set()
attribute_to_values = dict()

for _ in range(N):
    tmp = dict()
    input_list = list(input().split(","))
    for each in input_list:
        k, v = each.split("=")
        tmp[k] = v
        attributes.add(k)
        if k not in attribute_to_values:
            attribute_to_values[k] = set()
        attribute_to_values[k].add(v)
    db.append(tmp)

attributes = list(attributes)
attribute_combi = combinations(attributes, num_of_attri)


def recursive(atts, vs, idx, tmp):
    if idx == num_of_attri:
        cnt = 0
        for row in db:
            for k, v in tmp:
                if row[k] != v:
                    break
            else:
                cnt += 1
        if cnt / N >= support_thres:
            for k, v in tmp[:-1]:
                print(f"{k}={v},", end="")
            k, v = tmp[-1]
            print(f"{k}={v}")
        return
    if idx > num_of_attri:
        raise ValueError("Wrong")
    att = atts[idx]
    v = vs[idx]
    for each in v:
        tmp.append((att, each))
        recursive(atts, vs, idx + 1, tmp)
        tmp.pop()


for attribute in attribute_combi:
    atts = []
    vs = []
    for att in attribute:
        atts.append(att)
        vs.append(attribute_to_values[att])

    recursive(atts, vs, 0, [])
