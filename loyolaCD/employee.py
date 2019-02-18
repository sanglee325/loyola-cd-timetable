# -*- coding: utf-8 -*-
class Employee:
        def __init__(self):
                self.student_num = 0
                self.late = 0
                self.penalty = 0
                self.name = 'Name'
                self.major = 'Major'
                self.phone_num = 'PhoneNum'
                self.week = [['-']*5 for i in range(9)]
                self.weekend = ['-', '-']
                self.applied = 0 #total time apllied

        def __lt__(self, other):
                return self.penalty < other.penalty

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
                #mtwtf 0
                for i in range(5):
                        if self.week[0][i] == 'O':
                                avoid = 1
                                break
                #mon 1
                if self.week[1][0] == 'O':
                        avoid = 1
                #fri 678
                for i in range(3):
                        tmp = self.week[6+i][4]
                        if tmp[0] == 'O':
                                avoid = 1

                if avoid == 0:
                        self.penalty += 3
                if self.late > 0:
                        self.penalty += self.late*3
                if X == 0:
                        self.penalty -= 10000
                self.penalty -= X

        def count_apptime(self):
                count0 = 0
                count123456 = 0
                count78 = 0
                count_sat = 0

                for j in range(5):
                        if self.week[0][j] == 'O':
                                count0 += 1
                for i in range(6):
                        for j in range(5):
                                if self.week[i+1][j] == 'O':
                                        count123456 += 1.5
                for i in range(2):
                        for j in range(5):
                                if self.week[i+7][j] == 'O':
                                        count78 += 2
                for j in range(2):
                        if self.weekend[j] == 'O':
                                count_sat += 4
                                
                self.applied = count0 + count123456 + count78 + count_sat