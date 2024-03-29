"""
두 날짜(YYYYMMDD)의 차이 일수를 구하는 프로그램을 작성하시오.

※ 단, 프로그래밍 언어에서 지원하는 날짜차이를 계산하는 라이브러리는 사용하지 말것

예)
20070515 sub 20070501 = 14
20070501 sub 20070515 = 14
20070301 sub 20070515 = 75
"""
"""
========================================================================
과제1. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
        - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
        - first = 20070501
        - second = 20070515
        - 출력값 : 14
========================================================================
"""

first_date = int(input('첫 번째 날짜를 입력하세요 : '))         # first_date = 첫 번째 날짜 입력받을 때, 숫자(정수)로 변환
second_date = int(input('두 번째 날짜를 입력하세요 : '))        # second_date = 두 번째 날짜 입력받을 때, 숫자(정수)로 변환

print(abs(first_date - second_date))                           # 두 날짜 간 차이의 절대값 출력
print()

"""
========================================================================
과제2. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
        - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
        - first = 20070301
        - second = 20070515
        - 출력값 : 75
========================================================================
"""

# 날짜를 일로 변경하는 프로그램 정의
def is_day_count(yyyymmdd):
    # year = 앞 네 자리를 슬라이스 하여 숫자(정수)로 변환
    year = int(yyyymmdd[:4])
    # ytod = 년도 - 1을 일로 변환 (윤년은 4년의 한 번씩이지만, 100으로 나누어 떨어질 땐 평년, 400으로 나누어 떨어질 땐 윤년)
    ytod = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    
    # month = 4, 5 위치를 슬라이스 하여 숫자(정수)로 변환
    month = int(yyyymmdd[4:6])
    # mtod = 월 - 1을 일로 변환
    mtod = 0
    for i in range(1, month):
        # 2월은 윤년과 평년을 구분하여 계산
        if i == 2:
            if year % 400 == 0:
                mtod += 29
            elif year % 100 == 0:
                mtod += 28
            elif year % 4 == 0:
                mtod += 29
            else:
                mtod += 28
        # 4, 6, 9, 11월은 30일
        elif i in [4, 6, 9, 11]:
            mtod += 30
        # 나머지 (1, 3, 5, 7, 8, 10, 12월)은 31일
        else:
            mtod += 31

    # day = 마지막 두 자리를 슬라이스 하여 숫자(정수)로 변환
    day = int(yyyymmdd[6:])

    # 모두 더한 후 반환    
    return ytod + mtod + day

# 두 날짜 간의 차이를 구하는 프로그램 정의
def is_date_sub(first_date, second_date):
    # 두 날짜 간 차이의 절대값 출력
    print(abs(is_day_count(first_date) - is_day_count(second_date)))

if __name__ == '__main__':
    first_date = input('첫 번째 날짜를 입력하세요 : ')         # first_date = 첫 번째 날짜 입력받을 때, 숫자(정수)로 변환
    second_date = input('두 번째 날짜를 입력하세요 : ')        # second_date = 두 번째 날짜 입력받을 때, 숫자(정수)로 변환

    is_date_sub(first_date, second_date)                      # 두 날짜 간의 차이를 구하는 프로그램 실행