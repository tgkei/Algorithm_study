def solution(input_array):
    left = [-1 for _ in range(len(input_array))]
    right = [-1 for _ in range(len(input_array))]
    left_mul = 1
    right_mul = 1
    for i in range(len(input_array)):
        left_mul *= input_array[i]
        right_mul *= input_array[-(i+1)]
        left[i] = left_mul
        right[-(i+1)] = right_mul
    answer = [-1 for _ in range(len(input_array))]
    
    answer[0] = right[1]
    answer[-1] = left[-2]
    for i in range(1, len(left)-1):
        answer[i] = left[i-1] * right[i+1]
    return answer

if __name__ == "__main__":
    input_array = [1,2,3,4,5]
    print(solution(input_array))