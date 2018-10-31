# -*- coding: utf-8 -*-
"""
Created on 2018/10/30 

@author: susmote
"""


import requests
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))
import login_account_cookies

if __name__ == '__main__':
    for i in range(0, len(login_account_cookies.account_cookies)):
        session = requests.session()
        post_weibo_url = "https://m.weibo.cn/api/statuses/update"
        headers = {
            "Referer": "https://m.weibo.cn/compose/",
            "Cookie": login_account_cookies.account_cookies[i]
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
            print(i,"发微博成功")
        else:
            print(i,cmt_like_res_json["msg"])