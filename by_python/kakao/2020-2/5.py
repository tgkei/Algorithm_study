def parse_time(time):
    h, m, s = list(time.split(":"))
    return int(h) * 60 * 60 + int(m) * 60 + int(s)


def change_to_str(time):
    h = time//3600
    time = time % 3600
    m = time//60
    s = time % 60
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    if s < 10:
        s = "0" + str(s)
    else:
        s = str(s)

    return h+":"+m+":"+s


def solution(play_time, adv_time, logs):
    answer = ''
    longest = 0
    play_time = parse_time(play_time)
    adv_time = parse_time(adv_time)
    # print(play_time)
    # print(play_time - (adv_time-2) + adv_time)
    log_list = []
    for log in logs:
        start, end = map(parse_time, log.split('-'))
        log_list.append((start, end))
    log_list.sort()

    start_idx = 0
    for adv_s in range(play_time - (adv_time-1)):
        tmp = 0
        adv_e = adv_s + adv_time
        for idx, (log_s, log_e) in enumerate(log_list[start_idx:]):
            if log_e <= adv_s:
                start_idx = idx
                continue
            if log_s >= adv_e:
                break
            start = max(adv_s, log_s)
            end = min(adv_e, log_e)
            tmp += (end-start+1)
        if longest < tmp:
            longest = tmp
            answer = change_to_str(adv_s)

    return answer


if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00",
            "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

    print(solution(play_time, adv_time, logs))
