"""
위 그림은 {5,2,4,6,1,3} 이라는 배열을 소트하는 방법을 보여준다.
배열의 두번째 인덱스부터 시작하여 시작한 인덱스(검정색 블록) 좌측의 항목 중 자신이 들어가야 할 위치를 판단(소트되도록)하여 이동 한다.
좌측의 배열 요소들은 본인보다 좌측에 값이 삽입되어 들어올 경우 한칸씩 우측으로 이동한다. 단, 삽입되어 들어오는 요소(그림에서 검정색 블록)가 있던 인덱스(원래의 위치)까지만 이동한다.
마지막 인덱스까지 위 과정을 반복한다.
이와 같은 기능을 하는 소트 프로그램을 작성하시오.

그림 설명 : http://codingdojang.com/scode/443?answer_mode=hide
"""
"""
=============================================================================
과제 1. 위 문제의 알고리즘으로 배열을 정렬하시오. 
       - 조건 : 결과값을 저장하기 위해 새로운 리스트를 생성할 수 없다.
       - input = [5,2,6]
       - 출력 : [2,5,6]
=============================================================================
"""

n_list = list(map(int,input("배열 입력: ").split(",")))
for i in range(len(n_list)):
    for j in range(i+1,len(n_list)):  #1부터 2까지 두번
        if n_list[i] > n_list[j]:       #들어가야 할 위치인지 판단
            n_list.insert(i,n_list.pop(j))  #insert(위치, 입력할 데이터)특정 인덱스에 요소 추가
                                            #list.pop(인덱스)삭제한 뒤 삭제한 요소 반환, 즉 삭제한 뒤 insert로 추가 
print(n_list)

"""
=============================================================================
과제 2. 위 문제의 알고리즘으로 배열을 정렬하시오
       - 조건 : 결과값을 저장하기 위해 새로운 리스트를 생성할 수 없다.
       - input = [5,2,4,6,1,3]
       - 출력 : [1,2,3,4,5,6]
=============================================================================
"""
n_list = list(map(int,input("배열 입력: ").split(",")))
for i in range(len(n_list)):
    for j in range(i+1,len(n_list)):     #1부터 5까지
        if n_list[i] > n_list[j]:
            n_list.insert(i,n_list.pop(j))  #insert(위치, 입력할 데이터)특정 인덱스에 요소 추가
                                            #list.pop(인덱스)삭제한 뒤 삭제한 요소 반환, 즉 삭제한 뒤 insert로 추가 
print(n_list)