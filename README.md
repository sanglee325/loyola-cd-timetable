# loyolaCDtimetable
* Loyola library CD student employees' timetable setting program

1. Automatically makes timetable during the semester
2. Uses openpyxl (must be installed before used)
    ~~~bash
    C:\> pip install openpyxl
    ~~~
3. Furthermore, to use program in any computer make it into .exe
    ~~~bash
    C:\> pip install pyinstaller
    C:\> cd [directory]
    C:\> pyinstaller -F -n loyolaCDtime.exe create_timetable.py
    ~~~
    __loyolaCDtime.exe__ will contain libraries imported

### 사용법 및 주의사항 [KOR]
1. __신청서__ 폴더에 받은 20XX-0X_학번_이름.xlsx 엑셀 파일들을 넣는다.
2. __loyolaCDtime.exe__ 실행 전 현재 위치에서 __loyolaCD__ 와 __신청서__ 폴더, 그리고 __result.xlsx__ 파일이 있는지를 확인한다. (첨부된 zip파일에는 필요한 파일들이 모두 있다.)
3. __loyolaCDtime.exe__ 를 실행한다
    

### HOW TO USE [ENG]
1. Put 20XX-0X_20XXXX_[NAME].xlsx files in the __신청서__ directory.
2. Before executing the __loyolaCDtime.exe__ check if __loyolaCD__, __신청서__ directory, and __result.xlsx__ exist. (Attachted zip file contains all above.)
3. Execute __loyolaCDtime.exe__

