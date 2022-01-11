# A+B - 4

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 각 테스트 케이스마다 A+B를 출력한다.

# EOF(End Of File)-파일의 끝. 빈 문자열, 입력이 끝날 때까지 A+B를 출력하는 문제
# 참고: https://www.acmicpc.net/board/view/28913

while True:
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)

        print(a + b)
    except EOFError:    # EOF를 만났을 때
        break

