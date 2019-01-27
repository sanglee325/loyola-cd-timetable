import openpyxl
import employee as E

# 현재 Active Sheet 얻기
# ws = wb.active
def open_sheet(filename, new, wb, ws):
        #filename에서 데이터 split, 저장
        tmp = filename.split('_')
        tt = tmp[2].split('.')

        new.student_num = tmp[1]
        new.name = tt[0]
        new.major = ws['E22'].value
        new.phone_num = ws['G22'].value


def read_timetable(new, wb, ws):
        #주중 시간표 읽어오기
        for i in range(5):
                for j in range(9):
                        new.week[i][j] = ws.cell(row=26+j, column=5+i).value
        #주말 읽어오기
        for j in range(2):
                new.weekend[0][j] = ws.cell(row=38+i, column=5).value


def count_p(new, ws):
        #x의 갯수
        for i in range(5):
                for j in range(9):
                        tmp = new.week[i][j].split('(')
                        if tmp[0] == 'X':
                                new.X += 1
        for j in range(2):
                tmp = new.week[0][j].split('(')
                if tmp[0] == 'X':
                        new.X += 1

        #지각 페널티
        late = ws['I39'].value
        new.late = int(late)

        #기피 근무시간대 체크 여부
        for i in range(5):
                tmp = new.week[0][i]





