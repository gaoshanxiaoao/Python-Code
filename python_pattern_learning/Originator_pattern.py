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
