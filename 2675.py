# 문자열 반복

# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
# 각 테스트 케이스에 대해 P를 출력한다.

t = int(input())  # t: 테스트 케이스 개수 -> 1을 입력했을 경우

for i in range(t):
    p = []  # p: 각 문자를 r번 반복해 만들어진 새 문자열
    s = list(map(str, input().split()))  # 3 ABC 입력 -> ['3', 'ABC']
    r = int(s[0])  # 3

    for c in s[1]:   # s[1]에 있는 문자열을 쪼갬 -> ['A','B','C']
        for j in range(r):  # 3번 반복
            p.append(c)
            print(c, end='')  # AAABBBCCC
    print()
