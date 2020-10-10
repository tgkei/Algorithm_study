inf = int(1e9)


def convert(cur_time):
    times = cur_time.split(":")
    hour = int(times[0]) * 60 * 60
    minute = int(times[1]) * 60
    sec = int(times[2])
    return hour + minute + sec


def find_kiosks(customer, cur_time, spent_time, kiosks, cur_date):
    smallest = inf
    kiosk_num = -1
    cur_time = convert(cur_time) + cur_date
    for kiosk, end_time in enumerate(kiosks):
        if end_time < smallest:
            smallest = end_time
            kiosk_num = kiosk

    kiosks[kiosk_num] = cur_time + (int(spent_time) * 60)
    return kiosk_num


def convert_date_to_time(cur_date):
    tmp = cur_date.split("/")
    ret = int(tmp[0]) * 24*60*60 * 60
    ret += int(tmp[1]) * 24 * 60 * 60
    return ret


def solution(n, customers):
    answer = 0
    kiosks = [-1 for _ in range(n)]
    answers = [0 for _ in range(n)]

    for customer in customers:
        customer = customer.split(" ")
        cur_date, cur_time, spent_time = customer[0], customer[1], customer[2]
        cur_date = convert_date_to_time(cur_date)

        kiosk_num = find_kiosks(
            customer, cur_time, spent_time, kiosks, cur_date)
        answers[kiosk_num] += 1
    answer = max(answers)
    return answer


if __name__ == "__main__":
    n = 2
    customers = ["02/28 23:59:00 03", "03/01 00:00:00 02", "03/01 00:05:00 01"]
    print(solution(n, customers))
