'''
여기 배열이 하나 있습니다. 이 배열의 크기는 n으로 106을 넘지 않습니다. 그리고 이 배열의 왼쪽 끝에서 오른쪽 끝으로 움직이고 있는 슬라이딩 윈도우가 있습니다. 이 윈도우의 길이는 k입니다. 여러분은 윈도우 안에 보이는 k개의 수만을 볼 수 있습니다. 윈도우는 한 번에 한 칸씩 오른쪽으로 움직입니다. 다음은 예제입니다.

example

슬라이딩 윈도우가 각 위치에 있을 때 보이는 최대값과 최소값이 무엇인지 구하는 것이 여러분에게 주어진 문제입니다.

입력

입력은 두 개의 줄로 이루어져 있습니다. 첫 번째 줄은 배열의 길이와 슬라이딩 윈도우의 길이를 나타내는 두 개의 정수n과 k를 담고 있습니다. 다음 줄에 배열의 내용을 나타내는 n개의 정수가 담겨 있습니다.

출력

출력은 두 개의 줄을 담고 있어야 합니다. 첫 번째 줄은 윈도우가 왼쪽에서 오른쪽으로 움직일 때마다 윈도우에 보이는 최소값을 나타냅니다. 두번째 줄은 최대값입니다.

Sample Input

8 3
1 3 -1 -3 5 3 6 7
Sample Output

-1 -3 -3 -3 3 3
3 3 5 5 6 7
'''
"""
========================================================================
과제1. 아래와 같이 숫자 리스트와 슬라이딩윈도우의 크기가 주어졌을 때, 각각의 슬라이딩윈도우의 최소값과 최대값을 구하시오.
      - sliding_window_size = 3
      - num_list = [1, 3, -1, -3, 5, 3, 6, 7]
      - 최대값 : 3 3 5 5 6 7
      - 최소값 : -1 -3 -3 -3 3 3
========================================================================
"""

if __name__ == '__main__':
    k = int(input("sliding_window_size = "))                        # sliding_window_size 입력값을 정수로 변환후 k에 저장
    n_list = list(map(int, input("num_list = ").split(", ")))       # 입력받은 slicing_list를 ', '을 기준으로 나눈 후 map함수를 사용하여 
                                                                    # 각각의 요소들을 정수형으로 변환하여 n_list에 저장
    n = len(n_list)                                                 # n_list의 요소 개수 n에 저장

    max_output = []                                                 # 최대값과 최소값을 저장할 빈 리스트 생성
    min_output = []

    for i in range(n-k+1):                                          # slicing_window가 n-k+1개 생성되므로 for문 을 사용하여 n-k+1번 반복
        max_output.append(max(n_list[i:i+k]))                       # list를 slicing 하여 max 함수와 min 함수를 사용하여
        min_output.append(min(n_list[i:i+k]))                       # 최대값과 최소값을 각각의 리스트에 저장

    print('최대값:', *max_output)                                    # 결과 출력
    print('최소값:', *min_output)
