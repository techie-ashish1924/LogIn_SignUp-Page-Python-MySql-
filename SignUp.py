import pymysql
import os

os.system('cls')
def sign():

    connection_db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Ashish@24",
    database = "user_details"
    )
    try:
        with connection_db.cursor() as my_cursor:
            First_name = input("Enter your first name : ")
            Last_name = input("Enter your last name : ")
            Mob_no = int(input("Enter your mobile number : "))
            email_id = input("Enter your email id : ")
            password =input("Enter your password : ")

            sqll = "SELECT Mob from login_detail"
            my_cursor.execute(sqll)
            res = 1
            for mob in my_cursor:
                if mob[0] == Mob_no:
                    # return 0
                    res = 0
            # sql = "CREATE Table login_detail(First_name VARCHAR(25),Last_name VARCHAR(25),Mob BIGINT,email VARCHAR(40),password VARCHAR(10))"
            # my_cursor.execute(sql)
            if res == 0:
                return 0
            else:
                sql1 = "INSERT INTO login_detail(First_name,Last_name,Mob,email,password) VALUES(%s,%s,%s,%s,%s)"
                values = (First_name,Last_name,Mob_no,email_id,password)
                my_cursor.execute(sql1,values)
                sql2 = f"CREATE TABLE {First_name}(First_name VARCHAR(15),Last_name VARCHAR(15),amount BIGINT,Date VARCHAR(20),Interest BIGINT)"
                my_cursor.execute(sql2)
                connection_db.commit()
                return 1
    finally:
        connection_db.close()
    





    

