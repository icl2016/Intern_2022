'''
다음과 같은 형태의 배열을

[a1,a2,a3...,an,b1,b2...bn]
다음과 같은 형태로 바꾸시오

[a1,b1,a2,b2.....an,bn]
'''
"""
========================================================================
과제1. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 사용 X
      - input_list = [a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6] 
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

def q1():
    input_list = input('input_list = ').split(', ')             # input 값을 ', '를 기준으로 나눈 후 변수에 저장

    a = []                                                      # an을 저장해줄 빈 리스트 a 생성
    b = []                                                      # bn을 저장해줄 빈 리스트 a 생성
    output_list = []                                            # 결과값을 저장해줄 빈 리스트 생성

    for i in input_list:                                        # input_list에서
        if i[0] == 'a':                                         # 각 요소의 첫번째 자리가 a 이면
            a.append(i)                                         # 리스트 a에 저장
        if i[0] == 'b':                                         # 각 요소의 첫번째 자리가 b 이면
            b.append(i)                                         # b에 저장

    for i in range(len(a)):                                     
        output_list.append(a[i])                                # output_list에 a[i]를 먼저 추가해주고
        output_list.append(b[i])                                # b[i]를 차례대로 추가

    print(output_list)                                          # 결과값 출력

"""
========================================================================
과제2. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 필수적 사용
      - input_list = [a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6]
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

def q2():
    input_list = input('input_list = ').split(', ')                 # input 값을 ', ' 기준으로 나눈 후 변수에 저장

    output_list = sorted(input_list, key = lambda x: x[1])          # 각 요소의 첫번째 자리를 기준으로 오름차순정렬           

    print(output_list)                                              # 결과값 출력
    

"""
========================================================================
과제3. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 사용 X
      - input_list = [b1, a2, b3, a4, b5, a6, a1, b2, b4, a3, a5, b6]
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

def q3():
    input_list = input('input_list = ').split(', ')

    input_list.sort()                                               # 초기 input을 오름차순 정렬 (나머지는 과제1과 동일)

    a = []
    b = []
    output_list = []
    for i in input_list:
        if i[0] == 'a':
            a.append(i)
        if i[0] == 'b':
            b.append(i)

    for i in range(len(a)):
        output_list.append(a[i])
        output_list.append(b[i])

    print(output_list)


"""
========================================================================
과제4. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 필수적 사용
      - input_list = [b1, a2, b3, a4, b5, a6, a1, b2, b4, a3, a5, b6]
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

def q4():
    input_list = input('input_list = ').split(', ')         

    input_list.sort()                                               # 초기 input을 오름차순 정렬 (나머지는 과제2와 동일)

    output_list = sorted(input_list, key = lambda x: x[1])     

    print(output_list)    


if __name__ == '__main__':
      print('=====과제1=====')
      q1()
      print('=====과제2=====')
      q2()
      print('=====과제3=====')
      q3()
      print('=====과제4=====')
      q4()
