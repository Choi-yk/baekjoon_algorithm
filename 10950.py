# A+B - 3

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 각 테스트 케이스마다 A+B를 출력한다.

t = int(input())  # 변수 t에 테스트 개수를 입력받는다.

for i in range(t):  # 입력받은 값만큼 반복한다.
    i = input().split()
    print(int(i[0]) + int(i[1]))
