# -*- coding: utf-8 -*-
"""
Created on 2018/10/31 

@author: loyio
"""

import requests
import json

def fake_login(username, password, conn):
    login_url = "https://passport.weibo.cn/sso/login"
    c = conn.cursor()
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
    print(login_page_res.text)
    login_page_res_json = json.loads(login_page_res.text)
    print(login_page_res_json)
    judge_login_res = session.get("https://m.weibo.cn/api/config").text
    judge_login_res_json = json.loads(judge_login_res)
    if judge_login_res_json["data"]["login"] == True:
        print(1, "自动登录成功")
        cookie_str = ''
        for key in list(session.cookies.get_dict().keys()):  # 遍历字典
            cookie_str += (key + '=' + session.cookies.get_dict()[key] + ';')  # 将键值对拿出来拼接一下
        cmd = "UPDATE WeiboCookies SET COOKIES = \"" + cookie_str + "\" WHERE USERNAME = \"" + username + "\""
        c.execute(cmd)
        conn.commit()
    else:
        if login_page_res_json["msg"] == "用户名或密码错误":
            cmd = "UPDATE WeiboCookies SET TIPS = \"用户名或密码错误\" WHERE USERNAME = \"" + username + "\""
            c.execute(cmd)
            conn.commit()
            print("用户名或密码错误")
        else:
            cmd = "UPDATE WeiboCookies SET TIPS = \"需要进行人工验证\" WHERE USERNAME = \"" + username + "\""
            c.execute(cmd)
            conn.commit()
            print("不能直接登录,需要进行手势验证码验证")

