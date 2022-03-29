# 주사위 세개

# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 첫째 줄에 게임의 상금을 출력 한다.

a, b, c = map(int, input().split())

if a == b == c:  # 같은 눈이 3개일 경우
    cash = 10000 + a * 1000
elif a == b or a == c:
    cash = 1000 + a * 100
elif b == c:
    cash = 1000 + b * 100
else:  # 모두 다를 경우
    cash = max(a, b, c) * 100

print(cash)
