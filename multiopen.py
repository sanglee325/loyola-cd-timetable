import glob
import data as D
import employee as E
from openpyxl import load_workbook
from openpyxl import Workbook

xlsx_file = []

for filename in glob.glob('*.xlsx'):
    xlsx_file.append(filename)
print(xlsx_file)
tmp_student = E.Employee()
student = [E.Employee()]*len(xlsx_file)

for i in range(len(xlsx_file)):
    name = xlsx_file[i]
    app_wb = load_workbook(name)
    app_ws = app_wb.get_sheet_by_name("Sheet1")

    #load data to class student
    D.get_info(name, tmp_student, app_wb, app_ws)
    D.read_timetable(tmp_student, app_wb, app_ws)
    D.count_p(tmp_student, app_ws)

#    student[i].student_num = tmp_student.student_num
#    student[i].name = tmp_student.name
#    student[i].phone_num = tmp_student.phone_num
#    student[i].priority = tmp_student.priority
#    student[i].week = tmp_student.week
#    student[i].weekend = tmp_student.weekend


for i in range(len(xlsx_file)):
    print(student[i].student_num)