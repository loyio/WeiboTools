# -*- coding: utf-8 -*-
"""
Created on 2018/11/2 

@author: susmote
"""
import requests
import json
import sys
import time
import os

def auto_follow(uid, printToGui, conn):
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    c = conn.cursor()
    account_cookies = c.execute("SELECT * FROM WeiboCookies").fetchall()
    for i in range(0, len(account_cookies)):
        session = requests.session()
        follow_weibo_url = "https://m.weibo.cn/api/friendships/create"
        headers = {
            "Referer": "https://m.weibo.cn/search",
            "Cookie": account_cookies[i][4]
        }
        st_url = "https://m.weibo.cn/api/config"
        login_data = session.get(st_url, headers=headers).text
        login_data_json = json.loads(login_data)["data"]
        post_data = {
            "uid": uid,
            "st": login_data_json["st"]
        }
        auto_follow_res = session.post(follow_weibo_url, data=post_data, headers=headers)
        auto_follow_res_json = json.loads(auto_follow_res.text)
        if auto_follow_res_json["ok"] == 1:
            print(i+1," 关注", auto_follow_res_json["data"]["name"], "成功")
            printToGui(str(i+1)+" 关注"+auto_follow_res_json["data"]["name"]+"成功")
        else:
            print(i+1,auto_follow_res_json["msg"])
            printToGui(str(i+1)+auto_follow_res_json["msg"])
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print("共花费%d秒"%(end_time - begin_time))
    printToGui("共花费"+str(end_time-begin_time)+"秒")