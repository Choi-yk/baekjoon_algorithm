# A+B - 4

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 각 테스트 케이스마다 A+B를 출력한다.

# EOF(End Of File)-파일의 끝. 빈 문자열, 입력이 끝날 때까지 A+B를 출력하는 문제
# 참고: https://y00n-lee.tistory.com/9

while True:
    # try-catch문을 통해 예외처리를 한다.
    try:
        a, b = map(int, input().split())
        print(a + b)

    except:  # except 옆에 EOFError를 써도 된다.
        break  # 오류가 발생하면 While문이 멈춤
