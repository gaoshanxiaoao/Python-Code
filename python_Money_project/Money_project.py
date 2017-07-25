import MySql_operations as mos


class IWay:

    def update_record(self, money):
        pass

    def inquiry_record(self):
        pass


class User_Income_table(IWay):

    def update_record(self, money1, money2, money3):
        results = mos.mysql_operation(
            mos.Sql_list["sql_personal_accounts_income_insert"], money1, money2, money3)
        return results

    def inquiry_record(self):
        # print("hhhh")
        # print(mos.Sql_list["sql_personal_accounts_income_inquiry"])
        results = mos.mysql_operation(
            mos.Sql_list["sql_personal_accounts_income_inquiry"])
        # print(results)
        return results


class User_consume_table(IWay):

    def update_record(self, money1, money2):
        results = mos.mysql_operation(
            mos.Sql_list["sql_personal_accounts_concume_insert"], money1, money2)
        return results

    def inquiry_record(self, concume_type):
        results = mos.mysql_operation(
            mos.Sql_list["sql_personal_accounts_concume_inquiry"], concume_type)
        return results


class Context:

    def __init__(self, way):
        self.way = way

    def getRecord(self, *concume_type):
        # print(len(concume_type))
        if(len(concume_type) == 0):
            #print("hello world")
            return self.way.inquiry_record()
        else:
            return self.way.inquiry_record(concume_type[0])

    def updateRecord(self, *money):
        if(len(money) == 2):
            return self.way.update_record(money[0], money[1])
        else:
            return self.way.update_record(money[0], money[1], money[2])


#---------------------


class IManager:

    def getResult(self):
        pass

    def calculate(self):
        pass


class Income_per_Month(IManager):

    def __init__(self):
        self.Context = Context(User_Income_table())
        self.Accounts_income_balance_list = {}

    def calculate(self, income_money):
        daily_necessary_account, invest_account, play_account = Accounts_balance_calculation(
            income_money).calculate()
    # insert income to the table income
        print(daily_necessary_account)
        print(invest_account)
        print(play_account)
        results = self.Context.updateRecord(
            daily_necessary_account, invest_account, play_account)
        return results

    def getResult(self):
        self.Accounts_income_balance_list["daily_necessary_account"] = 0
        self.Accounts_income_balance_list["invest_account"] = 0
        self.Accounts_income_balance_list["play_account"] = 0
        results_dict = self.Context.getRecord()
        # print(results_dict)
        for key in self.Accounts_income_balance_list.keys():
            self.Accounts_income_balance_list[key] = results_dict[key]
        return self.Accounts_income_balance_list


class Concume_per_Month(IManager):

    def __init__(self):
        self.Context = Context(User_consume_table())
        self.concume_per_account_list = {}

    def getResult(self):
        self.concume_per_account_list["daily_necessary_account"] = 0
        self.concume_per_account_list["invest_account"] = 0
        self.concume_per_account_list["play_account"] = 0
        i = 1
        for key in self.concume_per_account_list.keys():
            results_dict = self.Context.getRecord(i)
            self.concume_per_account_list[
                key] = results_dict["total_concume_account"]
            i = i + 1
        return self.concume_per_account_list

    def calculate(self, concume_money, type_concume):
        results = self.Context.updateRecord(
            type_concume, concume_money)  # insert to the mysql
        return results


class Accounts_balance_calculation:

    def __init__(self, money):
        self.pretreat_money = money

    def calculate(self):
        return self.pretreat_money * 0.7, self.pretreat_money * 0.2, self.pretreat_money * 0.1


class Extra_per_Month(IManager):

    def __init__(self):
        self.accounts_extra = {}
        self.Income_per_Month = Income_per_Month()
        self.Concume_per_Month = Concume_per_Month()

    def getResult(self):
        return self.calculate()

    def calculate(self):
        accounts_income_list = self.Income_per_Month.getResult()
        # print(accounts_income_list)
        accounts_concume_list = self.Concume_per_Month.getResult()
        # print(accounts_concume_list)
        for key1 in accounts_concume_list.keys():
            if(accounts_concume_list[key1] == None):
                accounts_concume_list[key1] = 0
            for key2 in accounts_income_list.keys():
                if(key1 == key2):
                    if(key1 not in self.accounts_extra):
                        self.accounts_extra[key1] = 0
                    self.accounts_extra[key1] = accounts_income_list[
                        key2] - accounts_concume_list[key1]
        return self.accounts_extra
