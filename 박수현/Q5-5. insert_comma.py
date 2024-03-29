"""
숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로 바꾸어주는 프로그램을 작성하시오.

※ 단, 프로그래밍 언어에서 지원하는 금액변환 라이브러리는 사용하지 말것

예)
숫자	금액
1000	1,000
20000000	20,000,000
-3245.24	-3,245.24
"""
# input_money = float(input('금액을 입력하세요 : '))
# print('{:,}'.format(input_money))
"""
========================================================================
과제1. 아래와 같은 숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로 바꾸어주는 프로그램을 작성하시오.
        - 조건 : 파이썬의 금액변환 라이브러리 사용금지
        - money = 1000
        - 출력값 = 1,000
========================================================================
"""

input_money = input('금액을 입력하세요 : ')         # input_money = 입력받은 금액

print(f'{input_money[:-3]},{input_money[-3:]}')    # 뒤에서 세 자리를 슬라이스 하여 콤마 삽입 후 출력
print()

"""
========================================================================
과제2. 아래와 같은 숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로 바꾸어주는 프로그램을 작성하시오.
        - 조건 : 파이썬의 금액변환 라이브러리 사용금지
        - money = -3245.24
        - 출력값 = -3,245.24
========================================================================
"""

# 금액 표기식 문자열로 바꾸는 프로그램 정의
def is_money_w_comma(input_money):
    # 만약 길이가 4보다 작다면, 그대로 반환
    if len(input_money) < 4:
        return input_money
    # 만약 음수라면, '-' 제외하여 함수 실행
    if '-' in input_money:
        return f'-{is_money_w_comma(input_money[1:])}'
    # 만약 실수라면, '.' 위치부터 슬라이스 하여 함수 실행
    if '.' in input_money:
        return f'{is_money_w_comma(input_money[:input_money.index(".")])}{input_money[input_money.index("."):]}'
    # 만약 길이가 4보다 길다면, 뒤에서 세 자리를 슬라이스 하여 콤마 삽입 후 반환 (6보다 길다면 한 번 더 실행)
    if 4 <= len(input_money):
        return f'{is_money_w_comma(input_money[:-3])},{input_money[-3:]}'

if __name__ == '__main__':
    input_money = input('금액을 입력하세요 : ')         # input_money = 입력받은 금액

    print(is_money_w_comma(input_money))               # 금액 표기식 문자열로 바꾸는 프로그램 실행 후 반환값 출력