import pymysql

#with as 구문
#with (파일 경로, 모드) as 파일 객체
#파일을 열고 with as 구문이 끝날때 자동적으로 파일을 닫아준다 (close가 따로 필요없음)

conn = pymysql.connect(user='root',passwd='power900!', db='test2',charset='utf8')

def sign_up(sys_id,user_id,user_pw):
    try:
        with conn.cursor() as curs:
            signUp_sql = "insert into t_user values(%s,%s,%s)"
            if curs.execute(signUp_sql,(sys_id,user_id,user_pw)):
                print('Sign up Success')
                conn.commit()
            else:
                print('Sign up failed')

    except Exception as e:
        print(e)

def login_check(user_id,user_pw):
    try:
        with conn.cursor() as curs:
            user_check = [0,0]
            loginChk_sql = "select user_id,user_pw from t_user where user_id = %s or user_pw = %s"
            curs.execute(loginChk_sql,(user_id,user_pw))
            res = curs.fetchone()
            #res가 None일 경우 상정하지 않으면 값을 못읽었을 경우 오류
            if not res == None and user_id == res[0]:
                user_check[0] = 1
            if not res == None and user_pw == res[1]:
                user_check[1] = 1

            if user_check[0] and user_check[1]:
                return True
            else:
                return False
    except Exception as e:
        print(e)

def select_max_id_num():
    try:
        with conn.cursor() as curs:
            maxIdSql = "select MAX(id) from t_user"
            curs.execute(maxIdSql)
            maxIdNum = curs.fetchone()
            return maxIdNum[0]
    except Exception as e:
        print(e)
#
# def main():
    # print('select_max_id_num : ', select_max_id_num())
#     user_id = 'test1'
#     user_pw = 'test1'
#     login_check(user_id,user_pw)
#
# if __name__=='__main__': main()
