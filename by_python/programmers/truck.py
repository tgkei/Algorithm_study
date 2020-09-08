from queue import Queue


def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = Queue()
    for _ in range(bridge_length):
        q.put(0)

    truck_weights.reverse()
    current_weight = 0
    while not q.empty():
        answer += 1
        current_weight -= q.get()
        if not truck_weights:
            continue
        if current_weight + truck_weights[-1] <= weight:
            current_weight += truck_weights[-1]
            q.put(truck_weights.pop())
        else:
            q.put(0)

    return answer


if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    solution(bridge_length, weight, truck_weights)
