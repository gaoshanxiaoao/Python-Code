class Person:

    def Accept(self, visitor):
        pass


class Man(Person):

    def Accept(self, visitor):
        visitor.GetManConclusion(self)


class Woman(Person):

    def Accept(self, visitor):
        visitor.GetWomanConclusion(self)


class Action:

    def GetManConclusion(self, concreteElementA):
        pass

    def GetWomanConclusion(self, concreteElementB):
        pass


class Success(Action):

    def GetManConclusion(self, concreteElementA):
        print("when the man successes,he must have a great woman behind him")

    def GetWomanConclusion(self, conreteElementB):
        print("when the woman successes,she must have a bad man behind her")


class Failure(Action):

    def GetManConclusion(self, concreteElementA):
        print("when the man is fail, drink and no affect for advising")

    def GetWomanConclusion(self, concreteElementB):
        print("when the woman is fail, crying and no affect for advising")


class ObjectStructure:

    def __init__(self):
        self.plist = []

    def Add(self, p):
        self.plist.append(p)

    def Display(self, act):
        for p in self.plist:
            p.Accept(act)
