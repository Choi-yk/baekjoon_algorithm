# 빠른 A+B

# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

# 참고: https://ooyoung.tistory.com/34

import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b = sys.stdin.readline().split()  # 다른 문제들과 같이 split을 사용해 공백을 기준으로 잘라냄

    a = int(a)
    b = int(b)

    print(a + b)
