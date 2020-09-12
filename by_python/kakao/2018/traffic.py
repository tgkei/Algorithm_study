from math import ceil


def calc_start_time(line, which):
    tmp = list(line.split(" "))[1:]
    tmp[-1] = tmp[-1][:-1]
    end = tmp[0]
    start = tmp[0][:tmp[0].rfind(':')] + ":"
    time = tmp[0][tmp[0].rfind(':')+1:]
    start += str(round(float(time) - float(tmp[1]), 3)+0.001)

    hour = start[:start.find(':')]
    start = start[start.find(':')+1:]
    minute = start[:start.find(':')]
    second = round(float(start[start.find(':')+1:]), 3)
    duration = ceil(float(tmp[-1]))
    ret = int(((60*60*int(hour)) + (60*int(minute)) + second) * 1000)
    ret_arr = []
    while duration:
        ret_arr.append((ret, which))
        ret += 1000
        duration -= 1

    hour = end[:end.find(':')]
    end = end[end.find(':')+1:]
    minute = end[:end.find(':')]
    second = round(float(end[end.find(':')+1:]), 3)
    ret = int(((60*60*int(hour)) + (60*int(minute)) + second) * 1000)
    ret_arr.append((ret, which))
    return ret_arr


def solution(lines):
    answer = 0

    start_times = list()
    for which, line in enumerate(lines):
        start_time = calc_start_time(line, which)
        for each_time in start_time:
            start_times.append(each_time)

    start_times.sort(reverse=True)
    while start_times:
        fastest = start_times.pop()
        idx = len(start_times)-1
        cache = set()
        cache.add(fastest[1])
        if idx < 0:
            continue
        while idx >= 0 and fastest[0]+1000 > start_times[idx][0]:
            cache.add(start_times[idx][1])
            idx -= 1
        answer = max(answer, len(cache))

    return answer


if __name__ == "__main__":
    par = ["2016-09-15 00:00:03.000 3s",
           "2016-09-15 00:00:01.001 1s",
           "2016-09-15 00:00:02.001 1s"]
    print(solution(par))
