import pymysql

connection_db = pymysql.connect(

    host = "localhost",
    user = "root",
    password = "Ashish@24",
    database = "user_details",
    # table = "login_details"
)

with connection_db.cursor() as my_cursor:
    try:
        # sql = "CREATE Table login_detail(First_name VARCHAR(25),Last_name VARCHAR(25),Mob BIGINT,email VARCHAR(40),password VARCHAR(10))"
        # my_cursor.execute(sql)

        # sql = "ALTER TABLE login_detail ADD Mob VARCHAR(20)"
        # ALTER TABLE table_name MODIFY COLUMN column_name datatype;
        # my_cursor.execute("select * from login_detail")
        # my_cursor.execute("DROP TABLE ayush")
        # my_cursor.execute("SHOW tables")
        # s = "Ashish"
        # # t1 = tuple(s)
        # # print(t1)
        # for i in my_cursor:
        #     print(i[0])
        #     if i[0]==s.lower():
        #         print("yes")
        #     else:
        #         print("no")
        my_cursor.execute("SELECT Mob from login_detail")
        s = 7830057666
        # t1 = tuple(s)
        # print(t1)
        for i in my_cursor:
            print(i)
            if i[0]==s:
                print("yes")
                break
            else:
                print("no")
        # sql = "CREATE TABLE login_detail(First_name VARCHAR(25),Last_name VARCHAR(25),Mob BIGINT,email VARCHAR(40),password VARCHAR(10))"
        # my_cursor.execute(sql)
        # for table in my_cursor:
        #     print(table)
    # sql2 = "CREATE "
    
    finally:
        connection_db.close()