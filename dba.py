import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='#############', #your sql  password luca
                             db='nse_500',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM nse_500.companies"
        cursor.execute(sql)
        data=cursor.fetchall()


finally:
    connection.close()

for i in data:
    print(i.values())






