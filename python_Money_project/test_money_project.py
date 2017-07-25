import unittest
import Money_project as mp


class TestMoneyProject(unittest.TestCase):

    def test_extra_per_Month(self):
        print("--------------extra_balance--------------")
        epm = mp.Extra_per_Month()
        accounts_extra = epm.getResult()
        print(accounts_extra)
'''
 def test_concume_update_per_Month(self):
        # 1 daily_necessary_account 2 invest_account 3 play_account
        print("-------------concume_update--------------")
        cpm = mp.Concume_per_Month()
        results = cpm.calculate(
            90 + 170 + 18.90 + 72 + 21.60 + 15.50 + 14.70 + 5.50 + 15, 3)
        if(results == 0):
            print("success")
	def test_concume_update_per_Month(self):
        # 1 daily_necessary_account 2 invest_account 3 play_account
        print("-------------concume_update--------------")
        cpm = mp.Concume_per_Month()
        results = cpm.calculate(16.80, 3)
        if(results == 0):
            print("success")
    def test_income_update_per_Month(self):
        print("-----------income_update-------------------")
        ipm = mp.Income_per_Month()
        results = ipm.calculate(1460.97)
        if(results == 0):
            print("success")
    def test_extra_per_Month(self):
        print("--------------extra_balance--------------")
        epm = mp.Extra_per_Month()
        accounts_extra = epm.getResult()
        print(accounts_extra)

    def test_income_inquiry_per_Month(self):
        # print("hello world")
        print("-----------------income_inquiry----------------------")
        ipm = mp.Income_per_Month()
        # print("hello world")
        temp_list = ipm.getResult()
        print(temp_list)
    def test_concume_inquiry_per_Month(self):
        print("---------------------concume_inquiry----------------")
        cpm = mp.Concume_per_Month()
        temp_list = cpm.getResult()
        print(temp_list)
'''
unittest.main()
