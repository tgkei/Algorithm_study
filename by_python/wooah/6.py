from collections import defaultdict
from pprint import pprint


def solution(logs):
    solved_cache = defaultdict(int)
    problem_cache = defaultdict(list)
    score_cache = defaultdict(int)
    users = set()
    cache = dict()

    for log in logs:
        uid, problem, score = log.split(" ")
        problem, score = int(problem), int(score)
        solved_cache[uid] += 1
        score_cache[uid] += score
        problem_cache[uid].append(problem)
        users.add(uid)

    for uid, problems in problem_cache.items():
        problem_cache[uid] = sorted(problems)

    for user in users:
        cache[user] = dict()
        for user2 in users:
            if user == user2:
                continue
            if user not in cache:
                cache[user] = dict()
            cache[user][user2] = True

    solved_num_uid_cache = dict()
    for uid, num_solved in solved_cache:
        if num_solved < 5:
            continue
        if num_solved not in solved_num_uid_cache:
            solved_num_uid_cache[num_solved] = []
        solved_num_uid_cache[num_solved].append(uid)

    del solved_cache

    total_score_cache = dict()

    for uid, score in score_cache:
        if score not in total_score_cache:
            total_score_cache[score] = []
        total_score_cache[score].append(uid)

    del score_cache

    for solved, users in solved_num_uid_cache.items():
        pass


if __name__ == "__main__":
    logs = [
        "0001 3 95",
        "0001 5 90",
        "0001 5 100",
        "0002 3 95",
        "0001 7 80",
        "0001 8 80",
        "0001 10 90",
        "0002 10 90",
        "0002 7 80",
        "0002 8 80",
        "0002 5 100",
        "0003 99 90",
    ]
    solution(logs)
