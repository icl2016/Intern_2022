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

def insertion_sort(arr):
    for i in range(1, len(arr)): 
        for j in range(i-1, -1, -1): # range 역순으로 입력값 j
            if arr[j] == arr[j+1]:
                break
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)



arr = [5,2,6]
insertion_sort(arr)


"""
=============================================================================
과제 2. 위 문제의 알고리즘으로 배열을 정렬하시오
       - 조건 : 결과값을 저장하기 위해 새로운 리스트를 생성할 수 없다.
       - input = [5,2,4,6,1,3]
       - 출력 : [1,2,3,4,5,6]
=============================================================================
"""

def insertion_sort(arr):
    for i in range(1, len(arr)): 
        for j in range(i-1, -1, -1): # range 역순으로 입력값 j
            if arr[j] == arr[j+1]:
                break
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

arr = [5,2,4,6,1,3]
insertion_sort(arr)
