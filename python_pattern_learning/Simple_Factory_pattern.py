
# simple factory class


class Operation:

    def GetResult(self):
        pass


class OperationAdd(Operation):

    def GetResult(self):
        return self.op1 + self.op2


class OperationSub(Operation):

    def GetResult(self):
        return self.op1 - self.op2


class OperationMul(Operation):

    def GetResult(self):
        return self.op1 * sel.op2


class OperationDiv(Operation):

    def GetResult(self):
        try:
            return self.op1 / self.op2
        except Exception as e:
            print("error:divided by zero")
            return 0


class OperationUndef(Operation):

    def GetResult(self):
        print("Undfine operation")
        return 0


class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd()
    operation["-"] = OperationSub()
    operation["*"] = OperationMul()
    operation["/"] = OperationDiv()

    def createOperation(self, ch):
        if(ch in self.operation.keys()):
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op
