import SignUp
import LogIn
import time
import os

def sleeping(s):
    for i in s:
        print(i,end="")
        time.sleep(0.02)
    print()
sleeping("................Welcome to my Service....May I Help you!..........................")
def Login_Signup():
    inf = 1
    while inf:
        
        print("Press 1 for login \nPress 2 for signUp")
        ch = int(input())
        os.system('cls')
        if ch==1:
            ans = LogIn.LOGIN()
            # print("utput og login page ",ans)
            if ans:
                inf=0
                return 1
                # print("Login succefully...................")
            else:
                return 0
                # print("Invalid User name or password...")
        else:
            flag2 = 1
            ans_sign = SignUp.sign()
            while flag2:
                
            # print(ans_sign)
            # SignUp.sign()
                if ans_sign: 
                    sleeping("You have done succefully SignUp Process..............")
                    flag2=0
                    os.system('cls')
                    Login_Signup()
                    # return 1
                else:
                    print("UserAlready Exist")
                    print("You want to re SignUp \n1)YES \n2)NO")
                    ch1 = int(input())
                    if ch1==1:
                        os.system('cls')
                        ans_sign = SignUp.sign()
                    else:
                        flag2 = 0
                        return 0
        print("\n\nIf you want to go home Page\n1)Yes\n2)No")
        ch1 = int(input())
        if ch1 == 1:
            inf = 1
        else:
            inf = 0

# SignUp.sign()