class Originator:

    def __init__(self):
        self.state = ""

    def Show(self):
        print(self.state)

    def CreateMemo(self):
        return Memo(self.state)

    def SetMemo(self, memo):
        self.state = memo.state


class Memo:
    state = ""

    def __init__(self, ts):
        self.state = ts


class Caretaker:
    memo = ""

on = Originator()
on.state = "on"
on.Show()
c = Caretaker()
c.memo = on.CreateMemo()
on.state = "off"
on.Show()
# ghost the state
on.SetMemo(c.memo)
on.Show()
