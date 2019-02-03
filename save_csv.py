import glob
import data as D
import employee as E
from openpyxl import load_workbook
from openpyxl import Workbook
import csv

xlsx_file = []

for filename in glob.glob('신청서/*.xlsx'):
    xlsx_file.append(filename)
print(xlsx_file)


tmp_data = open('tmp_data.csv', 'w', encoding='euc-kr', newline='')
wr = csv.writer(tmp_data)
tmp_student = E.Employee()

total = [len(xlsx_file)]
wr.writerow(total)

for i in range(len(xlsx_file)):
    employee_data = []
    name = xlsx_file[i]
    app_wb = load_workbook(name)
    app_ws = app_wb.get_sheet_by_name("Sheet1")

    #load data to class student
    D.get_info(name, tmp_student, app_wb, app_ws)
    D.read_timetable(tmp_student, app_wb, app_ws)

    employee_data.append(tmp_student.name)
    employee_data.append(tmp_student.major)
    employee_data.append(tmp_student.student_num)
    employee_data.append(tmp_student.phone_num)
    employee_data.append(tmp_student.late)
    employee_data.append(tmp_student.week)
    employee_data.append(tmp_student.weekend)

    wr.writerow(employee_data)


tmp_data.close()