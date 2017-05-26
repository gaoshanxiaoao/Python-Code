import unittest
import Simple_Factory_pattern as sf


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

unittest.main()
