"""
2나 5로 나누어 떨어지지 않는 1 이상 10,000 이하의 정수 n이 주어졌는데, n의 배수 중에는 10진수로 표기했을 때 모든 자리 숫자가 1인 것이 있다.
그러한 n의 배수 중에서 가장 작은 것은 몇 자리 수일까?

Sample Input
3
7
9901

Sample Output
3
6
12
"""

"""
=============================================================================
과제 1. 2나 5로 나누어 떨어지지 않는 1 이상 10,000 이하의 정수는 모두 몇 개인지 구하시오
       - output : 4000
=============================================================================
"""
output_ = 0
for num in range(1,10001):        #1부터 10000까지
       if num % 2 != 0 and num % 5 != 0:    #2로도 5로도 나누어떨어지지 않을시
              output_ += 1              #결과값에 1 추가
print(output_)

"""
=============================================================================
과제 2. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수와 그 수의 자리수를 구하시오
       - input =  7
       - output = 111111 6
=============================================================================
"""
input_ = int(input('입력: '))
one = '1'             #1을 문자열 형태로 저장
while int(one) % input_ != 0: #정수로 변환, 입력받은 수로 나누어떨어지는지 확인
       one += '1'             #나누어떨어지지 않을시 1을 추가
print(one, len(one))          #1로 이루어진 가장 작은 배수, 자리수 출력


"""
=============================================================================
과제 3. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수의 자리수를 구하시오
       - input =  3, 7, 9901
       - output = 3, 6, 12
=============================================================================
"""
outputlst = []        #결과를 저장할 리스트 
input2_ = map(int,input('입력: ').split(', '))   #입력받은 값을 콤마 기준으로 분리, 정수로 변환하여 저장
for number in input2_:       #입력받은 값 하나씩 꺼냄
       one = '1'        #1부터 시작
       while int(one) % number != 0:  #정수로 변환, 입력받은 수로 나누어떨어지는지 확인
              one += '1'        #나누어떨어지지 않을시 1을 추가
       outputlst.append(str((len(one))))   #len으로 자리수를 문자열로 변환해 리스트에 추가
print(', '.join(outputlst))   #리스트를 콤마로 구분한 문자열 형태로 출력