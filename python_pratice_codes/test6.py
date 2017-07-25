import MySql_Connection_tool as mst

try:
    with mst.connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO personal_accounts_income (daily_necessary_account, invest_account, play_account) VALUES (%f, %f, %f)'
        cursor.execute(sql % (20.0, 20.0, 20.0))
        #results = cursor.fetchone()
        # print(results)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    mst.connection.commit()

finally:
    mst.connection.close()

'''
test1 = {}
test1['a'] = 1
test1['b'] = 2
test1['c'] = 3
test1['a'] = 5
print(test1)


list1 = test1.values()
total = 0
for value in list1:
    total += value
print(total)
'''
