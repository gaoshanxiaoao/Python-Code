class Target:

    def Request():
        print("common request")


class Adaptee(Target):

    def SpecificRequest(self):
        print("specific requset")


class Adapter(Target):

    def __init__(self, ada):
        self.adaptee = ada

    def Request(self):
        self.adaptee.SpecificRequest()
