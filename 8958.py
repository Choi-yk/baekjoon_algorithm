# OX퀴즈

# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
# 각 테스트 케이스마다 점수를 출력한다.

n = int(input())  # 테스트 케이스 개수 입력

for i in range(n):
    quiz = list(input())

    score = 0  # score: 'O'의 개수를 카운트
    sum_score = 0  # sum_score: for 문을 돌면서 score의 값을 누적함
    for j in quiz:
        if j == 'O':
            score += 1  # 'O' 만날 때 score에 1씩 더하기
            sum_score += score  # 연속으로 맞았을 경우. sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)
