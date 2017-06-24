import unittest
import Simple_Factory_pattern as sf
import Strategy_pattern as sp
import Decorator_pattern as dp
import Propotype_pattern as pp
import copy
import Template_pattern as tp
import Facade_pattern as fp
import Observation_pattern as op


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

    def test_propotype_pattern(self):
        a = pp.Resume("a")
        b = a.Clone()
        c = copy.copy(a)
        d = copy.deepcopy(a)
        a.SetAge(7)
        b.SetAge(12)
        c.SetAge(15)
        d.SetAge(18)
        a.SetWorkExp("PrimarySchool", 1996)
        b.SetWorkExp("MidSchool", 2001)
        c.SetWorkExp("HighSchool", 2004)
        d.SetWorkExp("University", 2007)
        a.Display()
        b.Display()
        c.Display()
        d.Display()

    def test_template_pattern(self):
        s1 = tp.TestPaperA()
        s2 = tp.TestPaperB()
        print("Student 1")
        s1.TestQuestion1()
        s1.TestQuestion2()
        print("Student 2")
        s2.TestQuestion1()
        s2.TestQuestion2()

    def test_facade_pattern(self):
        f1 = fp.Facade()
        f1.MethodA()
        f1.MethodB()

    def test_observer_pattern(self):
        p = op.Secretary()
        s1 = op.StockObserver("xh", p)
        s2 = op.NBAObserver("wyt", p)
        p.Attach(s1)
        p.Attach(s2)
        p.action = "WARNING:BOSS"
        p.Notify()

unittest.main()
