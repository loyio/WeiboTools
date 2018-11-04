# -*- coding: utf-8 -*-
"""
Created on 2018/11/4 

@author: susmote
"""
import time
import requests
import json

if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    begin_time = time.time()
    session = requests.session()
    post_weibo_url = "https://energy.tv.weibo.cn/aj/repost"
    headers = {
        "Referer": "https://energy.tv.weibo.cn/aj/repost?eid=10302&suid=5644764907&page_type=tvenergy_index_star",
        "Cookie": "_T_WM=ee0061b007ec1a6d374cf48e20d06836; WEIBOCN_FROM=1110006030; SUB=_2A2522uR5DeRhGeRK61EV8SjJyz2IHXVSJIwxrDV6PUJbkdAKLWT2kW1NU3rx-jN57drUWEQp2T1Mj1AVuq_1XasP; SUHB=02MerkzFrLu7Xy; SCF=AqAHzZ6ZHQVM9imqD36gR4h3iQYH1umZ6oAB6ksIkhpM-BfFZcNETgHt9eHaXhbXOnkvbKVnuPGqh7NE_TZX0Ok.; SSOLoginState=1541313578; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174"
    }
    post_data = {
        "mid": "4301539303030712",
        "text": "@火箭少女101_杨超越 我在#超新星全运会#为你加油！生而为赢，不惧挑战！",
        "follow": "5644764907",
        "eid": "10302",
        "suid": "5644764907",
        "page_type": "tvenergy_index_star"
    }
    repost_weibo_res = session.post(post_weibo_url, data=post_data, headers=headers)
    print(repost_weibo_res.text)
    repost_weibo_res_json = json.loads(repost_weibo_res.text)
    if repost_weibo_res_json["code"] == "100000":
        print("转发微博成功 ", repost_weibo_res_json["msg"])
    else:
        print(repost_weibo_res_json["msg"])
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    spend_time = end_time - begin_time
    print("共花费%d秒"%(spend_time))