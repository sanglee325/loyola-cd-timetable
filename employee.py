class Employee:
    def __init__(self):
        self.student_num = 0
        self.late = 0
        self.penalty = 0
        self.name = 'Name'
        self.major ='Major'
        self.phone_num = 'PhoneNum'
        self.week = [['-']*5 for i in range(9)]
        self.weekend =['-', '-']

    def count_p(self):
        #num of X
        X = 0
        for i in range(9):
                for j in range(5):
                        if self.week[i][j] == 'X':
                                #self.X += 1
                                X += 1
        for j in range(2):
                if self.weekend[j] == 'X':
                        #self.X += 1
                        X += 1

        #avoided time
        avoid = 0
        for i in range(5):
                tmp = self.week[0][i]
                if tmp[0] == 'O':
                        #self.avoid = 1
                        avoid = 1
                        break


        if tmp[0] == 'O':
                #new.avoid = 1
                avoid = 1

        for i in range(3):
                tmp = self.week[6+i][4]
                if tmp[0] == 'O':
                        #new.avoid = 1
                        avoid = 1
        #new.penalty()
        if avoid == 0:
            self.penalty += 3
        if self.late > 0:
            self.penalty += self.late*3
        self.penalty -= X


