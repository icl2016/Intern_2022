#========================================================================
#다음과 같은 형태의 배열을
#[a1,a2,a3...,an,b1,b2...bn]
#다음과 같은 형태로 바꾸시오
#[a1,b1,a2,b2.....an,bn]
#========================================================================
#과제1. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
#      - 조건1. 람다식 사용 X
#      - input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
#      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']

#과제 1 풀이
input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6'] #input_list에 값 저장
i = 1                                                         #i에 1 저장
input_list1 = []                                              #input_list1명의 빈리스트 형성
while i < 7:                                                  #while문을 통해 i가 7보다 작으면
    input_list1.append(input_list[i-1])                       #input_list1에 input_list의 i-1번째 자리 값을 추가
    input_list1.append(input_list[(len(input_list)//2)+i-1])  #input_list1에 input_list의 input_list1를 2로 나눈 몫에 i를 더하고 1을 뺀 자리의 값을 추가
    i = i+1                                                   #i에 i+1값 할당

print(input_list1)   #결과값 출력
#========================================================================
#과제2. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
#      - 조건1. 람다식 필수적 사용
#      - input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
#      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']

#과제 2 풀이
input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6'] #input_list에 값 할당
print(sorted(input_list, key=lambda x: int(x[1:])))                        #input_list와 key=lambda x: int(x[1:]값을 새로운 리스트로 만들어 출력

#========================================================================
#과제3. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
#      - 조건1. 람다식 사용 X
#      - input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']
#      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']

#과제 3 풀이
input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']
i = 1                                                         #i에 1 저장
input_list1 = []                                              #input_list1명의 빈리스트 형성
while i < 7:                                                  #while문을 통해 i가 7보다 작으면
    input_list1.append(input_list[i-1])                       #input_list1에 input_list의 i-1번째 자리 값을 추가
    input_list1.append(input_list[(len(input_list)//2)+i-1])  #input_list1에 input_list의 input_list1를 2로 나눈 몫에 i를 더하고 1을 뺀 자리의 값을 추가
    i = i+1                                                   #i에 i+1값 할당

print(input_list1)   #결과값 출력
#========================================================================
#과제4. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
#      - 조건1. 람다식 필수적 사용
#      - input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6'] 
#      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']

#과제 4 풀이
input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']  #input_list에 값 할당
print(sorted(input_list, key=lambda x: int(x[1:])))                         #input_list와 key=lambda x: int(x[1:]값을 새로운 리스트로 만들어 출력

#========================================================================
