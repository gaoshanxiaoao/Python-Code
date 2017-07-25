import pymysql.cursors

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '463841965',
    'db': 'manager_money',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
#connection = pymysql.connect(**config)
