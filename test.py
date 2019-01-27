import openpyxl
import data as D
import employee as E

name = '2018-02_20171635_박상리.xlsx'
emp = E.Employee()

# 엑셀파일 열기
wb = openpyxl.load_workbook(name)
ws = wb.get_sheet_by_name("Sheet1")

D.open_sheet(name, emp, wb, ws)
D.read_timetable(emp, wb, ws)
D.count_p(emp, ws)

print(emp.name)
print(emp.student_num)