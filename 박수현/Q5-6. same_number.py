"""
문제
앞뒤가 같은 수는 바로 쓴 값과 거꾸로 쓴 값이 같은 수이다. 다음과 같은 예를 들 수 있다.
1
44
101
2002
8972798
1111111111111

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ... 과 같이, 0 이상의 앞뒤가 같은 수를 크기 순으로 나열할 때, n 번째 수를 계산하는 프로그램을 작성하라.

n은 1부터 시작하며 크기에는 제한이 없다.

입출력예
예 1) 1 => 0
예 2) 4 => 3
예 3) 30 => 202
예 4) 100 => 909
예 5) 30000 => 200000002
예 6) 1000000 => 90000000009
"""
"""
========================================================================
과제1. 앞뒤가 같은 수(n)를 크기순으로 나열하세요 (0 <= n <= 100).
        - 출력값 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99
========================================================================
"""

num_list = []                           # num_list = 거꾸로 하여도 같은 값들의 리스트가 될 빈 리스트

for i in range(0, 100):                 # 0부터 100까지 다음 행위 반복
    i = str(i)                          # i를 문자로 변환
    if i == i[::-1]:                    # 만약 i와 거꾸로한 i가 같다면, num_list에 추가
        num_list.append(i)

print(', '.join(num_list))              # 거꾸로 하여도 같은 값들의 리스트 출력
print()

"""
========================================================================
과제2. 0 이상의 앞뒤가 같은 수를 크기순으로 나열하고 30,000번째 수를 출력하세요.
        - 출력값 : 200000002
========================================================================
"""

# [Done] exited with code=0 in 639.013 seconds

num_list = []                           # num_list = 거꾸로 하여도 같은 값들의 리스트가 될 빈 리스트
i = 0                                   # i = 시작은 0

while True:                             # 다음 행위 무한 반복
    if len(num_list) == 30000:          # 만약 num_list의 길이가 30,000이 된다면, 30,000번째 수 출력 후 종료
        print(num_list[-1])
        break

    if str(i) == str(i)[::-1]:          # 만약 문자 i와 거꾸로한 i가 같다면, num_list에 추가
        num_list.append(i)
    i += 1                              # i에 1을 더하기