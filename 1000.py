# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A+B를 출력한다.

# 입력받은 값을 split 함수를 통해 공백을 기준으로 잘라 준다. a(공백)b => [a, b]
a, b = input().split()

# 수 a, b를 정수로 변환
a = int(a)
b = int(b)

print(a + b)
