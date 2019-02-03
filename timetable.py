import employee as E

class times:
    def __init__(self):
        self.max = 0
        self.current = 0
        self.name = []
    
    def time0(self):
        self.max = 2
    
    def time1678(self):
        self.max = 3
    
    def time2345(self):
        self.max = 4

class timetable:
    def __init__(self):
        self.cell = [[times()]*5 for i in range(9)]

    def set_max(self):
        for i in range(9):
            for j in range(5):
                if i == 0:
                    self.cell[i][j].time0()
                elif 1 < i < 6:
                    self.cell[i][j].time2345()
                else:
                    self.cell[i][j].time1678()
