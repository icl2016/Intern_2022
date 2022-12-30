#-----------------  Question  -----------------
#우리 학교에는 복도 불을 켜고 끄는 마부(Mabu)라는 사람이 있다.
#전구마다 불을 켜고 끄는 스위치가 있다.
#불이 꺼져 있을 때 스위치를 누르면 불이 켜지고 다시 스위치를 누르면 불이 꺼진다.
#처음에는 모든 전구가 꺼져 있다.
#마부라는 사람은 특이한 행동을 한다.
#복도에 n개의 전구가 있으면, 복도를 n번 왕복한다.
#i번째 갈 때 그는 i로 나누어 떨어지는 위치에 있는 스위치만 누른다.
#처음 위치로 돌아올 때는 아무 스위치도 건드리지 않는다.
#i번째 왕복은 (이런 이상한 행동을 하면서) 복도를 한 번 갔다가 오는 것으로 정의된다.
#마지막 전구의 최종 상태를 알아내자.
#과연 그 전구는 켜져 있을까 아니면 꺼져 있을까?
#Input : 복도에 있는 n번째 전구를 나타내는 숫자가 입력된다. (2^32-1 이하의 정수가 입력된다.) 0은 입력의 끝을 의미하며 그 값은 처리하지 않는다.
#Output : 그 전구가 켜져 있으면 "yes"를, 꺼져 있으면 "no"를 출력한다. 테스트 케이스마다 한 줄에 하나씩 출력한다.
#----------------------------------------------
#과제 1 : 복도에 있는 n번째 전구의 최종 상태를 출력하시오.
#        - 조건 : 0은 입력의 끝을 의미하며 그 값은 처리하지 않는다.
#        input = [3, 6241, 8191, 0] (만약 전구번호가 3이면, 3번 왕복한 후의 전구상태를 출력하는 코드를 짜면 된다.)
#        출력 : (테스트 케이스마다 한 줄에 하나씩 출력해야함.)
#              no
#              yes
#             no

#우리 학교에는 복도 불을 켜고 끄는 마부(Mabu)라는 사람이 있다.
#전구마다 불을 켜고 끄는 스위치가 있다.
#불이 꺼져 있을 때 스위치를 누르면 불이 켜지고 다시 스위치를 누르면 불이 꺼진다.
#처음에는 모든 전구가 꺼져 있다.
#마부라는 사람은 특이한 행동을 한다.
#복도에 n개의 전구가 있으면, 복도를 n번 왕복한다.
#i번째 갈 때 그는 i로 나누어 떨어지는 위치에 있는 스위치만 누른다.
#처음 위치로 돌아올 때는 아무 스위치도 건드리지 않는다.
#i번째 왕복은 (이런 이상한 행동을 하면서) 복도를 한 번 갔다가 오는 것으로 정의된다.
#마지막 전구의 최종 상태를 알아내자.
#과연 그 전구는 켜져 있을까 아니면 꺼져 있을까?
#Input : 복도에 있는 n번째 전구를 나타내는 숫자가 입력된다. (2^32-1 이하의 정수가 입력된다.) 0은 입력의 끝을 의미하며 그 값은 처리하지 않는다.
#Output : 그 전구가 켜져 있으면 "yes"를, 꺼져 있으면 "no"를 출력한다. 테스트 케이스마다 한 줄에 하나씩 출력한다.

#과제 1 풀이
n = int(input("input = "))       #n에 input을 이용하여 외부값을 받고 이를 숫자로 변환하여 저장
ramp = {True:'yes', False:'no'}  #
state = False                    # off
for i in range(1, n+2):
  if n%i == 0:
    state = not(state)

print(ramp[state])
#----------------------------------------------
#과제 1 : 복도에 있는 n번째 전구의 최종 상태를 출력하시오.
#        - 조건 : 0은 입력의 끝을 의미하며 그 값은 처리하지 않는다.
#        input = [3, 6241, 8191, 0] (만약 전구번호가 3이면, 3번 왕복한 후의 전구상태를 출력하는 코드를 짜면 된다.)
#        출력 : (테스트 케이스마다 한 줄에 하나씩 출력해야함.)
#              no
#              yes
#              no

#과제 2 풀이 
n = int(input("input = "))
ramp = {True:'yes', False:'no'}
state = False # off
for i in range(1, n+2):
  if n%i == 0:
    state = not(state)

print(ramp[state])
#----------------------------------------------
