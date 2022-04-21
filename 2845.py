# 파티가 끝나고 난 뒤

l, p = map(int, input().split())  # l: 사람의 수, p: 파티가 열렸던 곳의 넓이
party = list(map(int, input().split()))

m = l * p
gap = 0  # 상근이가 계산한 참가자의 수와 각 기사에 적혀있는 참가자의 수의 차이를 출력하기 위해 사용

for i in range(len(party)):
    gap = party[i] - m
    print(gap, end=' ')
