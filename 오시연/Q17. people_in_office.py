"""
-----------------  Question  -----------------
A사무실에는 특정일자의 출퇴근 시간이 기록된 거대한 로그파일이 있다고 한다.
파일의 형식은 다음과 같다. (한 라인에서 앞부분은 출근시간(HH:MM:SS), 뒷부분은 퇴근시간이다)
- 09:12:23 11:14:35
- 10:34:01 13:23:40
- 10:34:31 11:20:10
특정시간을 입력(예:11:05:20)으로 주었을 때 그 시간에 총 몇 명이 사무실에 있었는지 알려주는 함수를 작성하시오.
----------------------------------------------
"""
"""
=============================================================================
과제 1. 'DATA\\Q3. people_in_office'폴더 내에 있는 '출퇴근기록.txt'를 읽어들이고, 
        주어진 시간(check_time)에 총 몇명이 사무실에 있었는지 알려주는 함수를 작성하시오.
        - check_time = "11:05:20"
        - 출력 : 4
=============================================================================
"""


t = ''.join(input('check_time: ').split(':') )    #입력받은 시간을 구분자 없이 붙임
count = 0       #사람 수
        
with open("python_seminar/DATA/Q3. people_in_office/commute_daily_log.txt", 'r') as f:  #파일을 읽기 모드로 읽고 자동으로 파일 닫기
        while True:       
                line = f.readline()           #무한 루프 안에서 파일의 문자열 한 줄씩 읽어들이기
                if not line:
                        break                 #더 이상 읽을 줄이 없으면 종료
                time_ = [''.join(x.split(':')) for x in line.split() ]   #한 줄을 공백 기준 분리>:를 기준으로 분리>구분자 없이 붙여서 리스트에 넣음                                   
                if time_[0] <= t <= time_[1]:            #입력한 시간이 출근, 퇴근 시간 안에 속하면 1 추가
                        count += 1        
print(count)
