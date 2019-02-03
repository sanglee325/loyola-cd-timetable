import read_csv as rcsv
#import employee as E
import timetable as tt
from openpyxl import load_workbook

schedule = tt.timetable()
schedule.set_max()

for student in rcsv.student:
    for i in range(9):
        for j in range(5):
            if schedule.cell[i][j].current < schedule.cell[i][j].max:
                if student.week[i][j] == 'O':
                    schedule.cell[i][j].name.append(student.name)
                    schedule.cell[i][j].current += 1


wb = load_workbook('result.xlsx')
ws1 = wb.active
ws1.title = "근무시간표"
'''
for i in range(2):
    for j in range(5):
        if i < schedule.cell[i][j].current:
            ws1.cell(row=3+i, column=3+j).value = schedule.cell[0][j].name[i]

for i in range(3):
    for j in range(5):
        if i < schedule.cell[i][j].current:
            ws1.cell(row=5+i, column=3+j).value = schedule.cell[1][j].name[i]

for k in range(4):
    for i in range(4):
        for j in range(5):
            if i < schedule.cell[i][j].current:
                ws1.cell(row=(8+4*k)+i, column=3+j).value = schedule.cell[2+k][j].name[i] 

for k in range(3):
    for i in range(3):
        for j in range(5):
            if i < len(schedule.cell[i][j].name):
                ws1.cell(row=(24+k*3)+i, column=3+j).value = schedule.cell[6+k][j].name[i]
'''

wb.save('result.xlsx')

