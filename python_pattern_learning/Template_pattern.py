class TestPaper:

    def TestQuestion1(self):
        print("Test1:A.B.C.D.")
        print("{0}".format(self.Answer1()))

    def TestQuestion2(self):
        print("Test2:A.B.C.D.")
        print("{0}".format(self.Answer2()))

    def Answer1(self):
        return ""

    def Answer2(self):
        return ""


class TestPaperA(TestPaper):

    def Answer1(self):
        return "A"

    def Answer2(self):
        return "B"


class TestPaperB(TestPaper):

    def Answer1(self):
        return "D"

    def Answer2(self):
        return "D"
