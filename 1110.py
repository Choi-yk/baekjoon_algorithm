# 더하기 사이클

# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

# 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
# 첫째 줄에 N의 사이클 길이를 출력한다.

# 참고: https://wook-2124.tistory.com/222

n = int(input())
new_n = n

count = 0
while True:
    # 예) 68을 입력했을 때
    ten_n = new_n // 10  # 68 // 10 = 6, 십의 자리
    one_n = new_n % 10  # 68 % 10 = 8, 일의 자리
    sum_n = (ten_n + one_n) % 10  # 십의 자리 + 일의 자리 = 6 + 8 = 14, 14 % 10 = "4"

    new_n = (one_n * 10) + sum_n  # (8 * 10) + 4 = 84,  새로운 수 생성

    count += 1

    if n == new_n:  # 원래 수(n)와 새로운 수(new_n)이 같아지면
        break   # 멈추기!

print(count)