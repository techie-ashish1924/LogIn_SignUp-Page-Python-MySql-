# import time
import pymysql 
import os

def login():
    mob = int(input("Enter your mobile number : "))
    Password = input("Enter your password : ")


    connection_db = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Ashish@24",
        database = "user_details"
    )
    try:
        with connection_db.cursor() as my_cursor:
            my_cursor.execute("select First_name,Last_name,Mob,Password from login_detail")
            for fname,lname,M,P in my_cursor:
                if M==mob and P==Password:
                    print("LogIn succefully.............")
                    print(f"Welcome {fname} {lname}")
                    return 1
                else:
                    # print("Invalid user name or password...")
                    return 0
    finally:
        connection_db.close()
    
def LOGIN():
    os.system('cls')
    flag = 1
    a=login()
    # print("output of login function ",a)
    while flag:
        if a:
            # print("Login Succefully................")
            flag = 0
            return 1
        else:
            print("Invalid user name or password...")
            print("You want to re login........\n1) Yes \n2)No")
            ch = int(input())
            if ch==1:
                os.system('cls')
                a=login()
            else:
                flag =0
                return 0
