def binary_search(arr, num):
    start = 0
    end = len(arr) - 1

    for small in range()
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

def four_sum(arr):
    ret = 0
    total = sum(arr)
    target = total //4

    arr = sorted(arr)

    for i in range(target+1):
        if binary_search(arr, target - i) and binary_search(arr, i):
            ret += 1
    
    return ret

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(four_sum)