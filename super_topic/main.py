# -*- coding: utf-8 -*-
"""
Created on 2018/11/5 

@author: susmote
"""

import time
import requests
import json




# 查看自己关注的超话

if __name__ == '__main__':
    followtopic_list = []
    url = "https://m.weibo.cn/api/container/getIndex?containerid=100803_-_followsuper"
    session = requests.session()
    headers = {
        "Host": "m.weibo.cn",
        "Referer": "https://m.weibo.cn",
        "Cookie": "_T_WM=708923df68a0352aef9f49395806ecf5; WEIBOCN_FROM=1110006030; SUB=_2A2522ueKDeRhGeVH6VMU-SjMzDmIHXVSJInCrDV6PUJbkdAKLVXckW1NT3_JWyQHEHoLRCNNaa-vtS7PHhgkYdKp; SUHB=0wn17vCTQ1QMLf; SCF=Aplj5FxFH0-WNZKC6UKEHOuQPqf_jTY5McD2blDumH_7pySahxyKcSlHvOh29xaYawIvm-TFZQ2zUXMu3InC1_o.; SSOLoginState=1541314522; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174"
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
                print("签到失败 "+res_json["data"]["msg"])