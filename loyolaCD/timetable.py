# -*- coding: utf-8 -*-
from loyolaCD import employee as E

class times:
    def __init__(self):
        self.max = 0
        self.current = 0
        self.name = []
        self.Xname = []
        self.blank = []
    
    def time0(self):
        self.max = 2
    
    def time1678(self):
        self.max = 3
    
    def time2345(self):
        self.max = 4

    def time_Sat(self):
        self.max = 3

class timetable:
    def __init__(self):
        self.cell = []
        self.sat = []

    def set_cell(self):
        for i in range(9):
            self.cell.append(list())
            for j in range(5):
                self.cell[i].append(times())

        for j in range(2):
            self.sat.append(times())

    def set_max(self):
        for i in range(9):
            for j in range(5):
                if i == 0:
                    self.cell[i][j].time0()
                elif 1 < i < 6:
                    self.cell[i][j].time2345()
                else:
                    self.cell[i][j].time1678()
        
        for j in range(2):
            self.sat[j].time_Sat()

def day_of_week(num):
   return ({0:"월", 1:"화", 2:"수", 3:"목", 4:"금", 5:"토"}.get(num, "default"))

def time_of_day(num):
    return ({0:"0교시", 1:"1교시", 2:"2교시", 3:"3교시", 4:"4교시", 5:"5교시", 6:"6교시", 7:"앞야", 8:"뒷야"}.get(num, "default"))