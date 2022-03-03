# 다이얼

# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

# 참고: https://ooyoung.tistory.com/73

d_list = ['', '', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
min_sec = 0
for i in d_list:
    for j in i:  # i에 있는 문자열을 쪼갬, ABC -> ['A','B','C']
        for k in a:  # a에서 입력받은 문자를 쪼갬, 'WA'를 입력했을 경우 -> ['W', 'A']
            if k == j:
                min_sec += d_list.index(i)
print(min_sec)
