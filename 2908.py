# 상수

# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
# 첫째 줄에 상수의 대답을 출력한다.

# 참고: https://ooyoung.tistory.com/72
# [::-1] 연산자 -> 문자를 역순으로 재배치함 (처음부터 끝까지 -1 간격으로)

arr = list(input().split())

arr[0] = int(arr[0][::-1])
arr[1] = int(arr[1][::-1])

if arr[0] < arr[1]:
    print(arr[1])
else:
    print(arr[0])
