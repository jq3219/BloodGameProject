import pymysql


#with as 구문
#with (파일 경로, 모드) as 파일 객체
#파일을 열고 with as 구문이 끝날때 자동적으로 파일을 닫아준다 (close가 따로 필요없음)

conn = pymysql.connect(user='root',passwd='power900!', db='test2',charset='utf8')

def insert_sql(params):
    try:
        with conn.cursor() as curs:
            print(params)
            insert_sql = "insert into t_user values(%s,%s,%s)"
            curs.execute(insert_sql,params[0])
            conn.commit()
    finally:
        pass
        # conn.close()

def login_check(id_input,pw_input):
    try:
        with conn.cursor() as curs:
            loginChk_sql = "select user_id,user_pw from t_user where user_id = %s and user_pw = %s"
            curs.execute(loginChk_sql,(id_input,pw_input))

            if curs.fetchone() != None:
                return True
            else:
                return False
    finally:
        pass
    #     conn.close()

def select_max_id_num():
    try:
        with conn.cursor() as curs:
            maxIdSql = "select MAX(id) from t_user"
            curs.execute(maxIdSql)
            maxIdNum = curs.fetchone()
            return maxIdNum[0]
    finally:
        pass
    #     conn.close()
# 
# def main():
#     id_input = 'test1'
#     pw_input = 'test1'
#     login_check(id_input,pw_input)
#
# if __name__=='__main__': main()
