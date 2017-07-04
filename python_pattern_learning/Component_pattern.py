class Component:

    def __init__(self, strName):
        self.m_strName = strName

    def Add(self, com):
        pass

    def Display(self, nDepth):
        pass


class Leaf(Component):

    def Add(self, com):
        print("leaf can't add")

    def Display(self, nDepth):
        strtemp = ""
        for i in range(nDepth):
            strtemp = strtemp + "-"
        strtemp = strtemp + self.m_strName
        print(strtemp)


class Composite(Component):

    def __init__(self, strName):
        super(strName)
        #self.m_strName = strName
        self.c = []

    def Add(self, com):
        self.c.append(com)

    def Display(self, nDepth):
        strtemp = ""
        for i in range(nDepth):
            strtemp = strtemp + "-"
        strtemp = strtemp + self.m_strName
        print(strtemp)
        # Recursive call when the com is Composite objective
        for com in self.c:
            com.Display(nDepth + 2)
