class Context:

    def __init__(self):
        self.input = ""
        self.output = ""


class AbstractExpression:

    def Interpret(self, context):
        pass


class Expression(AbstractExpression):

    def Interpret(self, context):
        print("terminal interpret")


class NonterminalExpression(AbstractExpression):

    def Interpret(self, context):
        print("Nonterminal interpret")
