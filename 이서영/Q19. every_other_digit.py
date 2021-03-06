"""
모든 짝수번째 숫자를 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.) 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.
Example: a1b2cde3~g45hi6 → a*b*cde*~g4*hi6
"""


"""
=============================================================================
과제 1. 짝수번째 자리에 숫자가 나올경우 *로 치환하는 프로그램을 작성하시오.(정규식 사용 금지)
       input = a1b2cde3~g45hi6
       출력 : a*b*cde*~g4*hi6
=============================================================================
"""

a= "a1b2cde3~g45hi6"
print("".join(['*' if (a[i].isdigit() and (i+1)%2 == 0 ) else a[i] for i in range(len(a))]))

"""
=============================================================================
과제 2. 짝수번째 자리에 숫자가 나올경우 *로 치환하는 프로그램을 작성하시오.(정규식 사용)
       input = a1b2cde3~g45hi6
       출력 : a*b*cde*~g4*hi6
=============================================================================
"""

import re                                               # 정규표현식 re 모듈

input = 'a1b2cde3~g45hi6'
input = list(input)                                     # 테스트 문자를 리스트로 변환

for i in range(len(input)):
    if i % 2 == 1:                                      # 리스트는 0부터 시작, 짝수번째 자리를 찾기위해서 나머지가 1인 부분 찾기
        input[i] = re.sub('\d', '*', input[i])          # 정규표현식을 이용하여 변환
                                                        # re.sub('[바꿀문자들]','어떤 것으로 바꿀건지', 문자열)


result = ''.join(input)                                 # 출력을 위한 join

print(result)

'''
\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.
'''