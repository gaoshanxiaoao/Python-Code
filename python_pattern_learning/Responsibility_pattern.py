class Request:

    def __init__(self, tcontent, tnum):
        self.content = tcontent
        self.num = tnum


class Manager:

    def __init__(self, temp):
        self.name = temp

    def SetSuccessor(self, temp):
        self.manager = temp

    def GetRequest(self, req):
        pass


class CommonManager(Manager):

    def GetRequest(self, req):
        if(req.num >= 0 and req.num < 10):
            print("{0} handled {1} request".format(self.name, req.num))
        else:
            self.manager.GetRequest(req)


class MajorDomo(Manager):

    def GetRequest(self, req):
        if(req.num >= 10):
            print("{0} handled {1} request".format(self.name, req.num))
