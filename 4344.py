# 평균은 넘겠지

# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 참고: https://mayuntel.tistory.com/18(퍼센트 기호 출력), https://ooyoung.tistory.com/62
# 문자열 포매팅을 알아야 한다. 파이썬 3.6 이상(f-string) https://ooyoung.tistory.com/87

c = int(input())  # c: 테스트 케이스의 개수, 입력

for i in range(c):  # 각 테스트 케이스마다 학생의 수가 첫 수로 주어짐
    n_score = list(map(int, input().split()))  # 학생의 수, 학생의 수만큼 각 점수가 저장되는 리스트
    avg_score = sum(n_score[1:]) / n_score[0]  # avg_score: 평균 점수. 점수 합계 / 학생의 수

    avg_cnt = 0  # avg_cnt: 평균 점수보다 점수가 높은 학생의 수 세기
    for j in n_score[1:]:
        if j > avg_score:
            avg_cnt += 1
    avg_rate = avg_cnt / n_score[0] * 100  # 평균 점수보다 점수가 높은 학생의 수 / 전체 학생의 수 * 100
    # print(f'{avg_rate:.3f}%')  # 문자열 포매팅할 경우
    print("%.3f" % avg_rate + "%")
