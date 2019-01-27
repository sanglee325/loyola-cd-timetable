class Employee:
    def __init__(self):
        self.student_num = 0
        self.name = 'Name'
        self.major ='Major'
        self.phone_num = 'PhoneNum'
        self.X = 0
        self.avoid = 0
        self.priority = 0
        self.late = 0

    def penalty(self):
        if self.avoid < 1:
            self.priority -= 3
        if self.late > 0:
            self.priority -= self.late*3
        self.priority += self.X

    def timetable(self, week, weekend):
        self.week = week
        self.weekend = weekend