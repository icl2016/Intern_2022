#==========================================================================
# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# n을 d(n)의 제네레이터(generator)라고 한다.
# 예를 들어 d(91) = 9 + 1 + 91 = 101인 경우 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
#==========================================================================
# 과제 1. 1부터 30까지의 자연수 중에서, 제너레이터가 있는 수의 합을 구하시오. 
## 출력 : 359

# 과제 1 풀이
def d(n):                   # def()함수로 정의
    for i in str(n):        # for문을 통해 n을 문자열으로 변환/반복
        n += int(i)         # n에 i를 숫자로 변환해 더하고 저장
    return n                # n값 반환

i0 = []                     # i0는 제너레이터를 추가할 빈 리스트
for i in range(1, 31):      # i의 범위는 1, 30까지 반복
    if d(i) <= 30:          # if문을 이용해 d(i)의 제네레이터가 30보다 같거나 작으면 리스트에 첨가
        i0.append(d(i))     # append를 통해 d(i)을 i0 리스트에 첨가

print(sum(i0))              # 변수 i0 값을 print
print(sum)                  # 변수 sum print
#==========================================================================
# 과제 2. 1이상 5000 미만의 셀프 넘버(제너레이터가 하나도 없는 수)의 합을 구하시오.
## 출력 : 1227365

# 과제 2 풀이
# d(n)을 정의
def d(n):                   # def()함수로 정의
    for i in str(n):        # for문을 통해 n을 문자열으로 변환/반복
        n += int(i)         # n에 i를 숫자로 변환해 더하고 저장
    return n                # n값 반환

i0 = []                     # i0는 제너레이터를 추가할 빈 리스트
for i in range(1, 5001):    # i의 범위는 1, 5001까지 반복
    if d(i) < 5000:         # if문을 이용해 d(i)의 제네레이터가 5000보다 같거나 작으면 리스트에 첨가
        i0.append(d(i))     # append를 통해 d(i)을 result 리스트에 첨가

i1 = []                     # i1 = 셀프 넘버를 추가할 빈 리스트
for i in range(1, 5000):    # i의 범위는 1, 5001까지 반복
    if i not in i0:         # 만약 i0에 i가 없다면
        i1.append(i)        # append를 통해 i를 i1 리스트에 첨가

print(sum(i1))              # 변수 sum(i1) print
#==========================================================================
