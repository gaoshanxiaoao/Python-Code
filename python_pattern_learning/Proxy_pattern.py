class Interface:

    def Request(self):
        return 0


class RealSubject(Interface):

    def Request(self):
        print("Real request.")


class Proxy(Interface):

    def Request(self):
        self.real = RealSubject()
        self.real.Request()
