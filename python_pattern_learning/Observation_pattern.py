class Observer:

    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub

    def Update(self):
        pass


class StockObserver(Observer):

    def Update(self):
        print("{0} {1}, stop watching Stock and go on work!".format(
            self.name, self.sub.action))


class NBAObserver(Observer):

    def Update(self):
        print("{0}{1}, stop watching NBA and go on work!".format(
            self.name, self.sub.action))


class SecretaryBase:

    def __init__(self):
        self.Observers = []

    def Attach(self, new_observer):
        pass

    def Notify(self):
        pass


class Secretary(SecretaryBase):

    def Attach(self, new_observer):
        self.Observers.append(new_observer)

    def Notify(self):
        for p in self.Observers:
            p.Update()
