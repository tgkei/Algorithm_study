def dfs(cur, dest):
    global links

    if cur == dest:
        return 1

    ret = 0

    if cur in links:
        for next_dest in links[cur]:
            ret += dfs(next_dest, dest)

    return ret


def solution(depar, hub, dest, roads):
    global links
    links = dict()

    for (city1, city2) in roads:
        if city1 not in links:
            links[city1] = [city2]
        else:
            links[city1].append(city2)

    to_hub = 0
    to_dest = 0
    if depar in links:
        stack = links[depar]

        while stack:
            cur = stack.pop()
            if cur == hub:
                to_hub += 1
                continue
            if cur in links:
                stack += links[cur]

    if hub in links:
        stack = links[hub]

        while stack:
            cur = stack.pop()
            if cur == dest:
                to_dest += 1
                continue
            if cur in links:
                stack += links[cur]
    return to_hub * to_dest


if __name__ == "__main__":
    depar = "SEOUL"
    hub = "DAEGU"
    dest = "YEOSU"
    roads = [["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "DAEJEON"], ["SEOUL", "ULSAN"], ["DAEJEON", "DAEGU"],
             ["GWANGJU", "BUSAN"], ["DAEGU", "GWANGJU"], ["DAEGU", "BUSAN"], ["ULSAN", "DAEGU"], ["GWANGJU", "YEOSU"], ["BUSAN", "YEOSU"]]

    print(solution(depar, hub, dest, roads))

    depar = "ULSAN"
    hub = "SEOUL"
    dest = "BUSAN"
    roads = [["SEOUL", "DAEJEON"], ["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], [
        "DAEJEON", "GWANGJU"], ["SEOUL", "ULSAN"], ["DAEJEON", "BUSAN"], ["GWANGJU", "BUSAN"]]
    print(solution(depar, hub, dest, roads))
