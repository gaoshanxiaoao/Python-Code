import MySql_Connection_tool as mct

Sql_list = {
    'sql_personal_accounts_income_insert': 'INSERT INTO personal_accounts_income (daily_necessary_account, invest_account, play_account) VALUES (%f, %f, %f)',
    'sql_personal_accounts_income_inquiry': 'SELECT SUM(daily_necessary_account) as daily_necessary_account,SUM(invest_account) as invest_account,SUM(play_account) as play_account FROM personal_accounts_income',
    'sql_personal_accounts_concume_insert': 'INSERT INTO personal_accounts_concume (concume_type,concume_money) VALUES (%d,%f)',
    'sql_personal_accounts_concume_inquiry': 'SELECT SUM(concume_money) as total_concume_account FROM personal_accounts_concume where concume_type = %d'
}


def mysql_operation(sql, VALUE_1=None, VALUE_2=None, VALUE_3=None):
    connection = mct.pymysql.connect(**mct.config)
    try:
        with connection.cursor() as cursor:
            if(VALUE_3 != None):
                # print(VALUE_1)
                # print(VALUE_2)
                # print(VALUE_3)
                cursor.execute(sql % (VALUE_1, VALUE_2, VALUE_3))
                results = 0
            else:
                if(VALUE_2 != None):
                    cursor.execute(sql % (VALUE_1, VALUE_2))
                    results = 0
                else:
                    if(VALUE_1 != None):
                        cursor.execute(sql % (VALUE_1))
                        results = cursor.fetchone()
                    else:
                        #print("this step")
                        cursor.execute(sql)
                        results = cursor.fetchone()
        connection.commit()
        # print(results)
        return results
    finally:
        connection.close()
