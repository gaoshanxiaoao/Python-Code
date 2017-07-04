
# similar as the Adapter_pattern.


class State:

    def WriteProgram(self):
        pass


class NoonState(State):

    def WriteProgram(self, w):
        print("noon working")
        if (w.hour < 13):
            print("fun.")
        else:
            print("need to rest.")


class ForenoonState(State):

    def WriteProgram(self, w):
        if (w.hour < 12):
            print("morning working")
            print("energetic")
        else:
            w.SetState(NoonState())
            w.WriteProgram()


class Work:

    def __init__(self):
        self.hour = 9
        self.current = ForenoonState()

    def SetState(self, temp):
        self.current = temp

    def WriteProgram(self):
        self.current.WriteProgram(self)

mywork = Work()
mywork.hour = 9
mywork.WriteProgram()
mywork.hour = 14
mywork.WriteProgram()
