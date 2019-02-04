import read_csv as rcsv
import timetable as tt
from openpyxl import load_workbook

schedule = tt.timetable()
schedule.set_cell()
schedule.set_max()

#load O info from the data
for i in range(9):
    for j in range(5):
        for k in range(len(rcsv.student)):
            if rcsv.student[k].week[i][j] == 'O':
                schedule.cell[i][j].name.append(rcsv.student[k].name)
                schedule.cell[i][j].current = schedule.cell[i][j].current+1


wb = load_workbook('result.xlsx')
ws1 = wb.active
ws1.title = "근무시간표"

line = 0 #number of lines accumulated
for i in range(9):
    for j in range(5):
        if i > 0 and j == 0:
            line += schedule.cell[i-1][j].max
        for k in range(schedule.cell[i][j].max):
            if k < len(schedule.cell[i][j].name):
                ws1.cell(row=3+line+k, column=3+j).value = schedule.cell[i][j].name[k]
            else:
                ws1.cell(row=3+line+k, column=3+j).value = " "


wb.save('result.xlsx')

