# 셀프 넘버

# 입력은 없다.
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

# 참고: https://ooyoung.tistory.com/64
# 리스트로 하는 방법도 있음. 근데 이해할 때 헷갈리는 것 같아서 안함.

sn_set = set(range(1, 10001))
remove_set = set()

for i in sn_set:
    for j in str(i):
        i += int(j)  # i의 각 자릿수를 j에 넣어 i에 더해 준다. 즉, i는 생성자가 있는 숫자이다.

    if i <= 10000:
        remove_set.add(i)  # 생성자가 있는 숫자를 추가

sn_set = sn_set - remove_set  # 차집합의 성질을 이용하여 remove_set의 요소와 겹치는 것을 삭제

for n in sorted(sn_set):
    print(n)