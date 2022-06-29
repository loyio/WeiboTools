# -*- coding: utf-8 -*-
"""
Created on 2018/11/2 

@author: loyio
"""
import requests
import json
import sys
import time
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))
import login_account_cookies
import sqlite3
conn = sqlite3.connect("../weibo_account.db")
print("自动改名系统".center(30, "*"))

if __name__ == '__main__':
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    c = conn.cursor()
    account_cookies = c.execute("SELECT * FROM WeiboCookies").fetchall()
    for i in range(0, len(account_cookies)):
        session = requests.session()
        change_name_url = "https://m.weibo.cn/settingDeal/inforSave"
        headers = {
            "Referer": "https://m.weibo.cn/setting/nick",
            "Cookie": account_cookies[i][4]
        }
        st_url = "https://m.weibo.cn/api/config"
        login_data = session.get(st_url, headers=headers).text
        login_data_json = json.loads(login_data)["data"]
        post_data = {
            "screen_name": "晕车药数据工"+ login_data_json["uid"][3:10],
            "st": login_data_json["st"]
        }
        change_name_res = session.post(change_name_url, data=post_data, headers=headers)
        print(change_name_res.text)
        change_name_res_json = json.loads(change_name_res.text)
        if change_name_res_json["ok"] == 1:
            print(i+1,"改名成功为 ", change_name_res_json["userInfo"]["name"])
        else:
            print(i+1,change_name_res_json["msg"])
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print("共花费%d秒"%(end_time - begin_time))