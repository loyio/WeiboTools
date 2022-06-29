# -*- coding: utf-8 -*-
"""
Created on 2018/11/5 

@author: loyio
"""

import time
import requests
import json




# 查看自己关注的超话

if __name__ == '__main__':
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
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
    login_page_res_json = json.loads(login_page_res.text)
    judge_login_res = session.get("https://m.weibo.cn/api/config").text
    judge_login_res_json = json.loads(judge_login_res)
    cookie_str = ''
    if judge_login_res_json["data"]["login"] == True:
        print(1, "自动登录成功")
        for key in list(session.cookies.get_dict().keys()):  # 遍历字典
            cookie_str += (key + '=' + session.cookies.get_dict()[key] + ';')  # 将键值对拿出来拼接一下
    else:
        if login_page_res_json["msg"] == "用户名或密码错误":
            print("用户名或密码错误")
            exit()
        else:
            print(login_page_res_json)
            print("不能直接登录,需要进行手势验证码验证")
            exit()
    followtopic_list = []
    url = "https://m.weibo.cn/api/container/getIndex?containerid=100803_-_followsuper"
    session = requests.session()
    headers = {
        "Host": "m.weibo.cn",
        "Referer": "https://m.weibo.cn",
        "Cookie": cookie_str
    }
    followtopic_res = session.get(url, headers=headers)
    followtopic_res_json = json.loads(followtopic_res.text)
    for i in range(0, len(followtopic_res_json["data"]["cards"][0]["card_group"])):
        if followtopic_res_json["data"]["cards"][0]["card_group"][i]["card_type"] == "8":
            followtopic_list.append(followtopic_res_json["data"]["cards"][0]["card_group"][i])
    if followtopic_res_json["data"]["cardlistInfo"]["since_id"] != "":
        followtopic_url = url+"&since_id="+ followtopic_res_json["data"]["cardlistInfo"]["since_id"]
        res = session.get(followtopic_url, headers=headers)
        res_json = json.loads(res.text)
        for i in range(0, len(res_json["data"]["cards"][0]["card_group"])-1):
            if res_json["data"]["cards"][0]["card_group"][i]["card_type"] == "8":
                followtopic_list.append(res_json["data"]["cards"][0]["card_group"][i])
    for i in range(0, len(followtopic_list)):
        print(followtopic_list[i]["title_sub"])
        st_url = "https://m.weibo.cn/api/config"
        login_data = session.get(st_url, headers=headers).text
        login_data_json = json.loads(login_data)["data"]
        postdata = {
            "st": login_data_json["st"]
        }
        if followtopic_list[i]["buttons"][0]["scheme"] == False:
            continue
        else:
            checkin_url = "https://m.weibo.cn"+str(followtopic_list[i]["buttons"][0]["scheme"])
            print(checkin_url)
            res = session.post(checkin_url, data=postdata, headers=headers)
            res_json = json.loads(res.text)
            if res_json["ok"] == 1:
                print("签到成功 "+res_json["data"]["msg"])
            else:
                print("签到失败 "+res_json)