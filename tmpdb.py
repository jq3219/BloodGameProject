import pymysql

conn = pymysql.connect(
    user='root',
    passwd='power900!',
    host='127.0.0.1',
    db='test2',
    charset='utf8'
)

cursor = conn.cursor()

sql = "select * from T_USER"
cursor.execute(sql)

rows = cursor.fetchall()
print(rows)

conn.close()
