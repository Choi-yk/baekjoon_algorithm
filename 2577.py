# 숫자의 개수

# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

# 각 숫자가 몇 번 나왔는지 저장하기 위해 일차원 배열을 만드는 문제
# 참고: https://go-hard.tistory.com/96

a = int(input())
b = int(input())
c = int(input())

n = a * b * c  # 곱한 값
arr = list(str(n))

for i in range(10):
    print(arr.count(str(i)))  # count('문자') -> 문자열 중 일치하는 문자의 개수를 돌려준다.

# 나의 풀이 방식
arr_my = []
for j in str(n):
    arr_my.append(j)

print(arr.count('0'))
print(arr.count('1'))
print(arr.count('2'))
print(arr.count('3'))
print(arr.count('4'))
print(arr.count('5'))
print(arr.count('6'))
print(arr.count('7'))
print(arr.count('8'))
print(arr.count('9'))
