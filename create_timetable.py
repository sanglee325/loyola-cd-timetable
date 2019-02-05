from loyolaCD import read_csv as rcsv
from loyolaCD import timetable as tt
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
ws1 = wb.get_sheet_by_name("근무시간표")
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

for i in range(len(rcsv.student)):
    rcsv.student[i].count_apptime()
    ws1.cell(row=5+i, column=10).value = rcsv.student[i].name
    ws1.cell(row=5+i, column=11).value = rcsv.student[i].applied

#in sheet1 schedule and applied time are set

ws1 = wb.get_sheet_by_name("신청자")
ws1.title = '신청자'

for i in range(9):
    ws1.cell(row=2+i, column=1).value = tt.time_of_day(i)

for j in range(5):
    ws1.cell(row=1, column=2+j).value = tt.day_of_week(j)

for i in range(9):
    for j in range(5):
        ws1.cell(row=2+i, column=2+j).value = "/".join(schedule.cell[i][j].name)
        

wb.save('result.xlsx')

