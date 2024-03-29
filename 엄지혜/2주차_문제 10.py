#==========================================================================
# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 한다.
# - 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99)이다.
# - 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하여라.
#==========================================================================
# 과제 1. 세 자리 수를 곱해서 만들들 수 있는 가장 큰 대칭수를 구하시오.
## 출력 : 906609

# 과제 1 풀이
result = []                                # result를 빈 리스트 생성

for i in range(100, 1000):                 # for문을 이용해 100부터 999까지 반복
    for j in range(100, 1000):             # for문을 이용해 100부터 999까지 반복
        num = i*j                          # 변수 num에 i*j값 할당
        if str(num) == str(num)[::-1]:     # 처음부터 끝까지 -1간격으로 변수 num를 문자열로 변환하여 num를 문자열로 변환한 것이 같다면  
            result.append(num)             # append를 이용해 num을 result에 첨가

print(max(result))                         #결과 print

#==========================================================================
# 과제 2. 출력 값에 천자리 구분기호가 나오도록 변환해 보세요(format()함수 사용)
## 출력 : 906,609

# 과제 2 풀이
result = []                                # result를 빈 리스트 생성

for i in range(100, 1000):                 # for문을 이용해 100부터 999까지 반복
    for j in range(100, 1000):             # for문을 이용해 100부터 999까지 반복
        num = i*j                          # 변수 num에 i*j값 할당
        if str(num) == str(num)[::-1]:     # 처음부터 끝까지 -1간격으로 변수 num를 문자열로 변환하여 num를 문자열로 변환한 것이 같다면  
            result.append(num)             # append를 이용해 num을 result에 첨가

print(format(max(result), ","))            # format으로 결과값에 ,추가하여 프린트

#==========================================================================
