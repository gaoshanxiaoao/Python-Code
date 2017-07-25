import unittest
import Simple_Factory_pattern as sf
import Strategy_pattern as sp
import Decorator_pattern as dp
import Propotype_pattern as pp
import copy
import Template_pattern as tp
import Facade_pattern as fp
import Observation_pattern as op
import Adapter_pattern as ap
import Originator_pattern as orp
import Component_pattern as cp
import Visitor_pattern as vp
import State_pattern as stp
import Responsibility_pattern as rp
import Proxy_pattern as prp
import Mediator_pattern as mp
import Interpreter_pattern as ip
import Flyweight_pattern as flp
import Command_pattern as cop
import Bridging_pattern as bp


class TestPatterns(unittest.TestCase):

    def test_simple_factory_pattern(self):
        print("-------factory_pattern---------------------------")
        op = input("operator: ")
        opa = input("a: ")
        opb = input("b: ")
        factory = sf.OperationFactory()
        cal = factory.createOperation(op)
        cal.op1 = int(opa)
        cal.op2 = int(opb)
        print(cal.GetResult())

    def test_strategy_pattern(self):
        print("---------------strategy_pattern---------------")
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
        print("----------decorator_pattern----------------")
        bt = dp.BigTrouser()
        ts = dp.TShirts()
        p = dp.Person("somebody")
        bt.Decorate(p)
        ts.Decorate(bt)
        ts.Show()

    def test_propotype_pattern(self):
        print("--------------propotype_pattern------------------")
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
        print("---------template_pattern---------------")
        s1 = tp.TestPaperA()
        s2 = tp.TestPaperB()
        print("Student 1")
        s1.TestQuestion1()
        s1.TestQuestion2()
        print("Student 2")
        s2.TestQuestion1()
        s2.TestQuestion2()

    def test_facade_pattern(self):
        print("------------facade_pattern----------------")
        f1 = fp.Facade()
        f1.MethodA()
        f1.MethodB()

    def test_observer_pattern(self):
        print("------------observer_pattern-------------")
        p = op.Secretary()
        s1 = op.StockObserver("xh", p)
        s2 = op.NBAObserver("wyt", p)
        p.Attach(s1)
        p.Attach(s2)
        p.action = "WARNING:BOSS"
        p.Notify()

    def test_adapter_pattern(self):
        print("-------------adapter_pattern----------------")
        adaptee = ap.Adaptee()
        adapter = ap.Adapter(adaptee)
        adapter.Request()

    def test_originator_pattern(self):
        print("-------------originator_pattern-----------------")
        on = orp.Originator()
        on.state = "on"
        on.Show()
        c = orp.Caretaker()
        c.memo = on.CreateMemo()
        on.state = "off"
        on.Show()
        # ghost the state
        on.SetMemo(c.memo)
        on.Show()

    def test_component_pattern(self):
        print("--------------component_pattern-------------------")
        p = cp.Composite("Wong")
        p.Add(Leaf("Lee"))
        p.Add(Leaf("Zhao"))
        p1 = cp.Composite("Wu")
        p1.Add(Leaf("San"))
        p.Add(p1)
        p.Display(1)

    def test_visitor_pattern(self):
        print("---------------visitor_pattern---------------")
        os = vp.ObjectStructure()
        os.Add(Man())
        os.Add(Woman())
        sc = vp.Success()
        os.Display(sc)
        fl = vp.Failure()
        os.Display(fl)

    def test_state_pattern(self):
        print("----------------state_pattern-----------------")
        mywork = stp.Work()
        mywork.hour = 9
        mywork.WriteProgram()
        mywork.hour = 14
        mywork.WriteProgram()

    def test_responsibility_pattern(self):
        print("--------------responsibility_pattern--------------")
        common = rp.CommonManager("Zhang")
        major = rp.MajorDomo("Lee")
        common.SetSuccessor(major)
        req = rp.Request("rest", 33)
        common.GetRequest(req)
        req2 = rp.Request("salary", 3)
        common.GetRequest(req2)

    def test_proxy_pattern(self):
        print("--------------------proxy_pattern------------------")
        p = prp.Proxy()
        p.Request()

    def test_mediator_pattern(self):
        print("-----------------mediator_pattern--------------------")
        m = mp.ConcreteMediator()
        col1 = mp.Collegue1(m)
        col2 = mp.Colleague2(m)
        m.col1 = col1
        m.col2 = col2
        col1.Send("How are you ?")
        col2.Send("Fine.")

    def test_interpreter_pattern(self):
        print("----------------interpreter_pattern-------------------")
        context = ""
        c = []
        c = c + [Expression()]
        c = c + [NonterminalExpression()]
        c = c + [Expression()]
        c = c + [Expression()]
        for a in c:
            a.Interpret(context)

    def test_flyweight_pattern(self):
        print("--------------flyweight_pattern--------------")
        f = flp.WebFactory()
        ws = f.GetWeb("blog")
        ws.Use("Lee")
        ws2 = f.GetWeb("show")
        ws2.Use("Jack")
        ws3 = f.GetWeb("blog")
        ws3.Use("Chen")
        ws4 = flp.UnShareWebSite("TEST")
        ws4.Use("Mr.Q")
        print(f.webtype)
        f.GetCount()

    def test_command_pattern(self):
        print("----------command_pattern-------------")

        barbucer = cop.Barbucer()
        cmd = cop.BakeMuttonCmd(barbucer)
        cmd2 = cop.ChickenWingCmd(barbucer)
        girl = cop.Waiter()
        girl.SetCmd(cmd)
        girl.SetCmd(cmd2)
        girl.Notify()

    def test_bridging_pattern(self):
        print("-------bridging_pattern----------")
        brand = bp.HandsetBrandM()
        brand.SetHandsetSoft(HandsetGame())
        brand.Run()
        brand.SetHandsetSoft(HandsetAddressList())
        brand.Run()


unittest.main()
