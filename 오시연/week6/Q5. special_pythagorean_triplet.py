'''
세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ). 예를 들면 3^2 + 4^2 = 9 + 16 = 25 = 5^2이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
'''
"""
========================================================================
과제1. 합이 1,000이고 아래 조건1,2를 만족하는 세 자연수 a,b,c의 곱을 구하시오.
      - 조건1. a < b < c 
      - 조건2. a^2 + b^2 = c^2 
      - 출력값1 : a=200 / b=375 / c=425
      - 출력값2 : 31,875,000
========================================================================
"""
for a in range(1, 500):  #499까지 a에 대입하며 반복
      for b in range(1, 1000 - a): #a를 뺀 범위까지 b에 대입하며 반복
            c = 1000 - (a + b)   #1000에서 a+b를 뺀 수를 c에 대입
            if a**2 + b**2 == c**2 and a < b < c: #만약 피타고라스 정리를 만족한다면
                  print('a={0} / b={1} / c={2}'.format(a, b, c)) #a,b,c의 값 출력
                  print(format(a * b * c, ',')) #a,b,c를 곱한 수를 천단위 구분하여 출력