def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0])

    end = routes[0][1]

    for route in routes[1:]:
        if route[0] > end:
            answer += 1
            end = route[1]
        else:
            end = min(route[1], end)

    answer = answer if answer else 1
    return answer


if __name__ == "__main__":
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(routes))
