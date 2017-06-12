import unittest
import Simple_Factory_pattern as sf
import Strategy_pattern as sp
import Decorator_pattern as dp


class TestPatterns(unittest.TestCase):

    def test_simple_factory_pattern(self):
        op = input("operator: ")
        opa = input("a: ")
        opb = input("b: ")
        factory = sf.OperationFactory()
        cal = factory.createOperation(op)
        cal.op1 = int(opa)
        cal.op2 = int(opb)
        print(cal.GetResult())

    def test_strategy_pattern(self):
        money = input("money:")
        strategy = {}
        strategy[1] = sp.CashContext(sp.CashNormal())
        strategy[2] = sp.CashContext(sp.CashRebate(0.8))
        strategy[3] = sp.CashContext(sp.CashReturn(300, 100))
        ctype = input(
            "type:[1]for normal,[2]for 80" + "\%" + " discount [3]for 300 -100.")
        if ctype in strategy:
            cc = strategy[ctype]
        else:
            print("Undefine type.Use normal mode.")
            cc = strategy[1]
        print("you will pay {0}%".format(cc.GetResult(money)))

    def test_decorator_pattern(self):
        bt = dp.BigTrouser()
        ts = dp.TShirts()
        p = dp.Person("somebody")
        bt.Decorate(p)
        ts.Decorate(bt)
        ts.Show()


unittest.main()
