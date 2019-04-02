number = input()
k = int(input())
number = list(number)
a = len(number)-k
result = []
s = 0
for i in range(a):
    maximum = max(number[s:k+i+1])
    """
    만약 10개중 4개를 뺀다면 1번째 숫자부터 4번째 숫자 중 가장 큰 값을 저장 및 그 값의 인덱스를 저장
    저장된 인덱스 부터 5번째 숫자 중 가장 큰 값 저장 및 인덱스를 업데이트 반복
    인덱스 업데이트시, 가장 큰 값의 인덱스 + 1에 인덱스가 0번부터가 시작하면 제일 처음 나오는 맥스 값에 대한 인덱스가
    나오므로 리스트를 잘라서 거기서 맥스값 구하고 이전의 인덱스 값을 더하는 방식 사용
    """
    s=(number[s:k+i+1].index(maximum))+1 + s 
    result.append(maximum)
answer = ''.join(result)
print(answer)