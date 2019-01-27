import openpyxl
import employee as E

# Get current Active Sheet
# ws = wb.active
def open_sheet(filename, new, wb, ws):
        #save data from filename
        tmp = filename.split('_')
        tt = tmp[2].split('.')

        new.student_num = tmp[1]
        new.name = tt[0]
        new.major = ws['E22'].value
        new.phone_num = ws['G22'].value


def read_timetable(new, wb, ws):
        #get week timetable
        for i in range(9):
                for j in range(5):
                        if ws.cell(row=26+i, column=5).value == None:
                                new.week[i][j] = '-'
                        else:
                                info = ws.cell(row=26+i, column=5+j).value
                                print info
                                tmp = info.split('(')
                                new.week[i][j] = tmp[0]
        #get weekend timetable
        for j in range(2):
                if ws.cell(row=38+j, column=5).value == None:
                        new.weekend[j] = '-'
                else:   
                        info = ws.cell(row=38+j, column=5).value
                        tmp = info.split('(')
                        new.weekend[j] = tmp[0]


def count_p(new, ws):
        new.week = [['0']*9 for i in range(5)]
        #num of X
        for i in range(5):
                for j in range(9):
                        tmp = new.week[i][j].split('(')
                        if tmp[0] == 'X':
                                new.X += 1
        for j in range(2):
                tmp = new.week[j][0].split('(')
                if tmp[0] == 'X':
                        new.X += 1

        #late penalty
        late = ws['I39'].value
        new.late = int(late)

        #avoided time
        for i in range(5):
                tmp = new.week[0][i].split('(')
                if tmp[0] == 'O':
                        new.avoid = 1
                        break

        tmp = new.week[1][0].split('(')
        if tmp[0] == 'O':
                new.avoid = 1

        for i in range(3):
                tmp = new.week[6+i][4].split('(')
                if tmp[0] == 'O':
                        new.avoid = 1
                        break
        new.penalty()

        





