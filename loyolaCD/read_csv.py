# -*- coding: utf-8 -*-
from loyolaCD import save_csv
import csv
from loyolaCD import data as D
from loyolaCD import employee as E

lines = 0
i = 0

student = []
with open('loyolaCD/tmp_data.csv', 'r') as f:
    reader_csv = csv.reader(f, delimiter=',')
    for row in reader_csv:
        if i == 0:
            lines = int(row[i])
            i = i + 1
        else:
            student.append(E.Employee())
            student[i-1].name = row[0]
            student[i-1].major = row[1]
            student[i-1].student_num = row[2]
            student[i-1].phone_num = row[3]
            student[i-1].late = int(row[4])
            D.divided_week(row[5], student[i-1].week)
            D.divided_weekend(row[6], student[i-1].weekend)
            student[i-1].count_p()
            i = i + 1
student.sort()

for i in range(lines):
    print(student[i].student_num)
    print(student[i].penalty)