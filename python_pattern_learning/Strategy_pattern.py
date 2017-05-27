# Strategy pattern


class CashSuper:

    def AcceptCash(self, money):
        return 0


class CashNormal(CashSuper):

    def AcceptCash(self, money):
        return 0


class CashRebate(CashSuper):
    discount = 0

    def __init__(self, ds):
        self.discount = ds

    def AcceptCash(self, money):
        return self.discount * money


class CashReturn(CashSuper):
    total = 0
    ret = 0

    def __init__(self, r, t):
        self.total = t
        self.ret = r

    def AcceptCash(self, moeny):
        if(money >= self.total):
            return money - self.ret
        else:
            return money


class CashContext:

    def __init__(self, csuper):
        self.cs = csuper

    def GetResult(self, money):
        return self.cs.AcceptCash(money)
