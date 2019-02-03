import read_csv as rcsv
#import employee as E
import timetable as tt
from openpyxl import load_workbook

schedule = tt.timetable()
schedule.set_max()

for k in range(len(rcsv.student)):
    for i in range(9):
        for j in range(5):
            if schedule.cell[i][j].current < schedule.cell[i][j].max:
                if rcsv.student[k].week[i][j] == 'O':
                    schedule.cell[i][j].name.append(rcsv.student[k].name)
                    schedule.cell[i][j].current += 1


wb = load_workbook('result.xlsx')
ws1 = wb.active
ws1.title = "근무시간표"

for i in range(2):
    for j in range(5):
        if i < schedule.cell[i][j].current:
            ws1.cell(row=3+i, column=3+j).value = schedule.cell[0][j].name[i]
        else:
            ws1.cell(row=3+i, column=3+j).value = " "

for i in range(3):
    for j in range(5):
        if i < schedule.cell[i][j].current:
            ws1.cell(row=5+i, column=3+j).value = schedule.cell[1][j].name[i]
        else:
            ws1.cell(row=5+i, column=3+j).value = " "

for k in range(4):
    for i in range(4):
        for j in range(5):
            if i < schedule.cell[i][j].current:
                ws1.cell(row=(8+4*k)+i, column=3+j).value = schedule.cell[2+k][j].name[i] 
            else:
                ws1.cell(row=(8+4*k)+i, column=3+j).value = " "

for k in range(3):
    for i in range(3):
        for j in range(5):
            if i < len(schedule.cell[i][j].name):
                ws1.cell(row=(24+k*3)+i, column=3+j).value = schedule.cell[6+k][j].name[i]
            else:
                ws1.cell(row=(24+k*3)+i, column=3+j).value = " "


wb.save('result.xlsx')

