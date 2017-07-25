class ioperator:

    def method1(self, argue1):
        print("hello")
        pass


class operator(ioperator):

    def method1(self, argue1, argue2):
        super().method1(argue1)
        print("successfull" + str(argue1) + str(argue2))

op = operator()
op.method1(2, 3)
