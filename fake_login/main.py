# -*- coding: utf-8 -*-
"""
Created on 2018/10/31 

@author: susmote
"""

import requests
import json
import sqlite3
conn = sqlite3.connect("../weibo_account.db")
c = conn.cursor()

if __name__ == '__main__':
    login_url = "https://passport.weibo.cn/sso/login"

    account_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
    headers = {
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F"
    }
    for i in range(0, len(account_list)):
        session = requests.session()
        login_post_data = {
            "username": account_list[i][1],
            # "username": "qzbidqzyaqxuy-gmtj@yahoo.com",
            "password": account_list[i][2],
            # "password": "ZXctojojcpd62",
            "savestate": "1",
            "r": "https://m.weibo.cn/",
            "ec": "0",
            "pagerefer": "https://m.weibo.cn/login?backURL=https%253A%252F%252Fm.weibo.cn%252F",
            "entry": "mweibo",
            "wentry": "",
            "loginfrom": "",
            "client_id": "",
            "code": "",
            "qq": "",
            "mainpageflag": "1",
            "hff": "",
            "hfp": ""
        }
        login_page_res = session.post(login_url, data=login_post_data, headers=headers)
        # login_page_res_json = json.loads(login_page_res.text)
        print(i+1, login_page_res.text)
        judge_login_res = session.get("https://m.weibo.cn/api/config").text
        judge_login_res_json = json.loads(judge_login_res)
        if judge_login_res_json["data"]["login"] == True:
            print(1, "自动登录成功")
            cookie_str = ''
            for key in list(session.cookies.get_dict().keys()):  # 遍历字典
                cookie_str += (key + '=' + session.cookies.get_dict()[key] + ';')  # 将键值对拿出来拼接一下
            c = conn.cursor()
            cmd = "UPDATE WeiboCookies SET COOKIES = \"" + cookie_str + "\" WHERE USERNAME = \"" + account_list[i][1] + "\""
            c.execute(cmd)
            conn.commit()
        else:
            print("不能直接登录,需要进行手势验证码验证")
        # postWeibo_data = {
        #     "content": "这是一条测试微博",
        #     "st": judge_login_res_json["data"]["st"]
        # }
        # post_weibo_res = session.post("https://m.weibo.cn/api/statuses/update", data=postWeibo_data, headers=headers)
        # print(json.loads(post_weibo_res.text))



def simulogin_session(username, password):
    login_url = "https://passport.weibo.cn/sso/login"
    headers = {
        "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F"
    }
    session = requests.session()
    login_post_data = {
        "username": username,
        "password": password,
        "savestate": "1",
        "r": "https://m.weibo.cn/",
        "ec": "0",
        "pagerefer": "https://m.weibo.cn/login?backURL=https%253A%252F%252Fm.weibo.cn%252F",
        "entry": "mweibo",
        "wentry": "",
        "loginfrom": "",
        "client_id": "",
        "code": "",
        "qq": "",
        "mainpageflag": "1",
        "hff": "",
        "hfp": ""
    }
    login_page_res = session.post(login_url, data=login_post_data, headers=headers)
    # login_page_res_json = json.loads(login_page_res.text)
    print(i + 1, login_page_res.text)
    judge_login_res = session.get("https://m.weibo.cn/api/config").text
    judge_login_res_json = json.loads(judge_login_res)
    if judge_login_res_json["data"]["login"] == True:
        print(1, "自动登录成功")
        return session
    else:
        print("不能直接登录,需要进行手势验证码验证")
        return False