class IUser:

    def GetUser(self):
        pass

    def InsertUser(self):
        pass


class IDepartment:

    def GetDepartment(self):
        pass

    def InsertDepartment(self):
        pass


class CAccessUser(IUser):

    def GetUser(self):
        print("Access GetUser")

    def InsertUser(self):
        print("Access InsertUser")


class CAccessDepartment(IDepartment):

    def GetDepartment(self):
        print("Access GetDepartment")

    def InsertDepartment(self):
        print("Access InsertDepartment")


class CsqlUser(IUser):

    def GetUser(self):
        print("Sql GetUser")

    def InsertUser(self):
        print("Sql InsertUser")


class CsqlDepartment(IDepartment):

    def GetDepartment(self):
        print("Sql GetDepartment")

    def InsertDepartment(self):
        print("Sql InsertDepartment")


class IFactory:

    def CreateUser(self):
        pass

    def CreateDepartment(self):
        pass


class AccessFactory(IFactory):

    def CreateUser(self):
        temp = CAccessUser()
        return temp

    def CreateDepartment(self):
        temp = CAccessDepartment()
        return temp


class SqlFactory(IFactory):

    def CreateDepartment(self):
        temp = CsqlDepartment()
        return temp

    def CreateUser(self):
        temp = CsqlUser()
        return temp
