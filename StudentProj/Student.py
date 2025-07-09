from operator import truediv


class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


    def is_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
