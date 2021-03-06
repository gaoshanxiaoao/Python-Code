class Barbucer:

    def MakeMutton(self):
        print("Mutton")

    def MakeChickenWing(self):
        print("Chicken Wing")


class Command:

    def __init__(self, temp):
        self.receiver = temp

    def ExecuteCmd(self):
        pass


class BakeMuttonCmd(Command):

    def ExecuteCmd(self):
        self.receiver.MakeMutton()


class ChickenWingCmd(Command):

    def ExecuteCmd(self):
        self.receiver.MakeChickenWing()


class Waiter:

    def __init__(self):
        self.order = []

    def SetCmd(self, command):
        self.order.append(command)
        print("Add Order")

    def Notify(self):
        for cmd in self.order:
            cmd.ExecuteCmd()
