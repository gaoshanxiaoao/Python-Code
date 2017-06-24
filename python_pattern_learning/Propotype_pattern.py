import copy


class WorkExp:
    place = ""
    year = 0


class Resume:
    name = ''
    age = 0

    def __init__(self, n):
        self.name = n

    def SetAge(self, a):
        self.age = a

    def SetWorkExp(self, p, y):
        self.place = p
        self.year = y

    def Display(self):
        print(self.age)
        print(self.place)
        print(self.year)

    def Clone(self):
        return self
