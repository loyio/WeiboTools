# -*- coding: utf-8 -*-
"""
Created on 2018/10/28 

@author: susmote
"""

import requests
import time
import json


def getUesrInfo(userCheck, UidOrName, printToGui):
    session = requests.session()
    if userCheck == 0:
        user_link = "https://api.weibo.cn/2/profile?new_version=0&user_domain=n/" + UidOrName
        raw_user_info = session.get(user_link).text
        res_info_json = json.loads(raw_user_info)
        if res_info_json[list(res_info_json.keys())[1]] == 20003:
            printToGui("你输入的用户名有误")
        else:
            user_info_json = res_info_json["userInfo"]
            printToGui("微博用户名: " + user_info_json["name"])
            if (user_info_json["verified"] == True):
                printToGui("微博认证  : " + str(user_info_json["verified_reason"]))
            printToGui("微博关注数: " + str(user_info_json["friends_count"]))
            printToGui("微博粉丝数: " + str(user_info_json["followers_count"]))
            printToGui("微博等级:  " + str(user_info_json["urank"]))
            printToGui("微博主页链接: "+ "https://m.weibo.cn/u/"+str(user_info_json["id"]))
    elif userCheck == 1:
        user_link = "https://m.weibo.cn/profile/info?uid=" + UidOrName
        raw_user_info = session.get(user_link).text
        res_info_json = json.loads(raw_user_info)
        if res_info_json["ok"] != 1:
            printToGui("你输入的用户名有误")
        else:
            user_info_json = res_info_json["data"]["user"]
            printToGui("微博用户名: " + user_info_json["screen_name"])
            if (user_info_json["verified"] == True):
                printToGui("微博认证  : " + str(user_info_json["verified_reason"]))
            printToGui("微博关注数: " + str(user_info_json["follow_count"]))
            printToGui("微博粉丝数: " + str(user_info_json["followers_count"]))
            printToGui("微博等级:  "+ str(user_info_json["urank"]))
            printToGui("微博主页链接: " + "https://m.weibo.cn/u/" + str(user_info_json["id"]))
    else:
        user_link = "https://api.weibo.cn/2/profile?new_version=0&user_domain=n/火箭少女101_杨超越"