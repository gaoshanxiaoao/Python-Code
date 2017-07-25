import sys


class WebSite:

    def Use(self):
        pass


class ConcreteWebSite(WebSite):

    def __init__(self, strName):
        self.name = strName

    def Use(self, user):
        print("Website type: {0} users:{1}".format(self.name, user))


class UnShareWebSite(WebSite):

    def __init__(self, strName):
        self.name = strName

    def Use(self, user):
        print("UnShare Website type:{0} users:{1}".format(self.name, user))


class WebFactory:

    def __init__(self):
        test = ConcreteWebSite("test")
        self.webtype = {"test": test}
        self.count = {"test": 0}

    def GetWeb(self, webtype):
        if webtype not in self.webtype:
            temp = ConcreteWebSite(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] = 1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] = self.count[webtype] + 1
        return temp

    def GetCount(self):
        for key in self.webtype:
            print("type:{0},count:{1}".format(key, self.count[key]))
