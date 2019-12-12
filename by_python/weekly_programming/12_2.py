"""
간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.

Given a list of intervals, merge intersecting intervals.
 
예제)
Input: {{2,4}, {1,5}, {7,9}}
Output: {{1,5}, {7,9}}

Input: {{3,6}, {1,3}, {2,4}}
Output: {{1,6}}
"""
def solve(Input):
    ret = []
    input_sorted = sorted(Input)
    idx = 1
    start = input_sorted[0][0]
    end = input_sorted[0][1]
    while idx < len(input_sorted):
        if end < input_sorted[idx][0]:
            ret.append([start,end])
            start = input_sorted[idx][0]
        end = max(input_sorted[idx][1],end)
        idx+=1
    ret.append([start,end])
    return ret

if __name__ == "__main__":
    Input = [[3,6], [1,3], [2,4]]
    print(solve(Input))