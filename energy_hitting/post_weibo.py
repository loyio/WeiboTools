# -*- coding: utf-8 -*-
"""
Created on 2018/10/30 

@author: susmote
"""


import requests
import json
import sys
import time
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))
import login_account_cookies
print("批量发微博系统".center(30, "*"))

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("请加上微博组号")
    else:
        begin_time = time.time()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        if sys.argv[1] == "1":
            account_cookies = login_account_cookies.account_cookies_1
        elif sys.argv[1] == "2":
            account_cookies = login_account_cookies.account_cookies_2
        else:
            account_cookies = []
            print("没有这组号")
            exit()
        for i in range(0, len(account_cookies)):
            session = requests.session()
            post_weibo_url = "https://m.weibo.cn/api/statuses/update"
            headers = {
                "Referer": "https://m.weibo.cn/compose/",
                "Cookie": account_cookies[i]
            }
            st_url = "https://m.weibo.cn/api/config"
            login_data = session.get(st_url, headers=headers).text
            login_data_json = json.loads(login_data)["data"]
            post_data = {
                "content": "@火箭少女101_杨超越 我在#超新星全运会#为你加油！生而为赢，不惧挑战！//@火箭少女101_杨超越 :#超新星全运会#[米奇比心]#杨超越超新星全运会# #超新星全运会# http://t.cn/EzV5piM",
                "st": login_data_json["st"]
            }
            post_weibo_res = session.post(post_weibo_url, data=post_data, headers=headers)
            cmt_like_res_json = json.loads(post_weibo_res.text)
            if cmt_like_res_json["ok"] == 1:
                print(i+1,"发微博成功")
            else:
                print(i+1,cmt_like_res_json["msg"])
        end_time = time.time()
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        print("共花费%d秒"%(end_time - begin_time))