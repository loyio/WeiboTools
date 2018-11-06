# -*- coding: utf-8 -*-
"""
Created on 2018/11/2 

@author: susmote
"""

import sqlite3
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))
conn = sqlite3.connect("cookies.sqlite")
print("Opened database successfully")
c = conn.cursor()


#创建的数据库
c.execute('''CREATE TABLE WeiboCookies
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       USERNAME VARCHAR(50)   NOT NULL,
       PASSWORD VARCHAR(50)   NOT NULL,
       TIPS     VARCHAR(50),
       Cookies   VARCHAR(500),
       STATE    VARCHAR(20));''')


#c.execute("INSERT INTO WeiboCookies VALUES(NULL, '_T_WM=ee0061b007ec1a6d374cf48e20d06836; WEIBOCN_FROM=1110006030; SUB=_2A2523UfWDeRhGeVP41cW-C3Iwj6IHXVSPmmerDV6PUJbkdANLXTskW1NTMCS7B5_rGw_npFkAnuMSegP51hr4tMI; SUHB=0auw8il68vUbfx; SCF=AsXwK20GzEA4p0hcQ5BzHczE758LlNpjRwVw7ebXp7ybqzNJyw6pnfvRg_SP3EbAqPK9ft46_QFnpSHoHkBh5yw.; SSOLoginState=1540962183; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174');")
# text = c.execute("DELETE FROM WeiboCookies WHERE ID = 5")
# print(text.fetchall())

# for i in range(0, len(login_account_cookies.account_cookies_3)):
#     cmd = "INSERT INTO WeiboCookies VALUES(NULL, \'"+ login_account_cookies.account_cookies_3[i] +"\');"
#     c.execute(cmd)
#     conn.commit()

# cmd = "INSERT INTO WeiboCookies VALUES(NULL, \'"+ "13558860850" +"\', \'"+ "75CEDF6394100000" +"\', \"\", \"\", \"\");"
# cmd = "ALTER TABLE WeiboCookies ADD COLUMN STATE VARCHAR(20)"
# cmd = "DELETE FROM WeiboCookies WHERE TIPS = \"\""
# cmd = "SELECT * FROM WeiboCookies"
# c.execute(cmd)
# res = c.execute(cmd).fetchall()
# print(res)
# Account_list = c.execute(cmd).fetchall()
# for i in range(0, len(Account_list)):
#     print(Account_list[i][1])

with open('weiboAccount.txt', 'r') as f:
    while True:
        account = f.readline().strip()
        if account == "":
            break
        accout_list = account.split("----")
        cmd = "INSERT INTO WeiboCookies VALUES(NULL, \'" + accout_list[0] + "\', \'" + accout_list[1] + "\', \"\");"
        c.execute(cmd)
        conn.commit()
conn.commit()
conn.close()