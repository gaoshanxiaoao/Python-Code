class Mediator:

    def Send(self, message, col):
        pass


class Colleague:

    def __init__(self, temp):
        self.mediator = temp


class Collegue1(Colleague):

    def Send(self, message):
        self.mediator.Send(message, self)

    def Notify(self, message):
        print("Colleague1 get a message : {0}".format(message))


class Colleague2(Colleague):

    def Send(self, message):
        self.mediator.Send(message, self)

    def Notify(self, message):
        print("Colleague2 get a message : {0}".format(message))


class ConcreteMediator(Mediator):

    def Send(self, message, col):
        if(col == col1):
            col1.Notify(message)
        else:
            col2.Notify(message)
