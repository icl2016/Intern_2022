'''
심술쟁이 수는 2,3,5의 곱으로 만들 수 있는 수이다. 다음과 같은 순서의 수가 11개의 심술쟁이 수이다.
1,2,3,4,5,6,8,9,10,12,15,....
처음 수는 1로 시작하도록 한다. 입력은 받지 않고, <number> 에 1500번째 심술쟁이 수가 출력되게 한다.
Sample Output
The 1500'th ugly number is <number>.
답
859963392
(1550번째는 1093500000, 십만번째는 290142196707511001929482240000000000000)
'''
"""
========================================================================
과제1. 숫자 2,3,5의 곱으로 만들 수 있는 수 작은 순서대로 11개를 출력하시오. 
      - 출력 : 1,2,3,4,5,6,8,9,10,12,15
========================================================================
"""

numbers = 0
lst = 0
numberlst = []

for numbers in range(1, 10000):
    if numbers % 2 == 0 or numbers % 3 == 0 or numbers % 5 == 0:
        lst += 1
        numberlst.append(numbers)
        if lst == 11:
            numberlst.insert(0, 1)
            break
print(numberlst)

"""
========================================================================
과제2. 숫자 2,3,5의 곱으로 만들 수 있는 수를 오름차순으로 정렬할 경우 1550번째 값을 구하시오. 
      - 출력 : 1,093,500,000
========================================================================
"""

def ugly(n):
    ugly_list = [1]
    j = 2
    while len(ugly_list) < n:
        i = j
        while i % 2 == 0: #2로 나눠지면
            i = int(i/2) #i는 2로 다시 한 번 나눠진다.
        while i % 3 == 0: #3으로 나눠지면
            i = int(i/3) #i는 3으로 다시 한 번 나눠진다
        while i % 5 == 0: #5으로 나눠지면
            i = int(i/5) #i는 5으로 다시 한 번 나눠진다.
        if i == 1: #즉, 소인수분해 2, 3, 5가 가능하면
            ugly_list.append(j) #심술쟁이 수로서 리스트에 넣는다.
        j = j + 1 #j를 1을 추가해서 계속해서 반복한다.

print(ugly(1550))