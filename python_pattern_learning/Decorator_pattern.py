class Person:

    def __init__(self, tname):
        self.name = tname

    def Show(self):
        print("dressed {0}".format(self.name))


class Finary(Person):
    componet = None

    def __init__(self):
        pass

    def Decorate(self, ct):
        self.componet = ct

    def Show(self):
        if(self.componet != None):
            self.componet.Show()


class TShirts(Finary):

    def __init__(self):
        pass

    def Show(self):
        print("Big T-shirt")
        # self.componet.Show()
        super().Show()


class BigTrouser(Finary):

    def __init__(self):
        pass

    def Show(self):
        print("Big Trouser")
        # self.componet.Show()
        super().Show()

bt = BigTrouser()
ts = TShirts()
p = Person("somebody")
bt.Decorate(p)
ts.Decorate(bt)
ts.Show()
