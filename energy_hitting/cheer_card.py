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
    session = requests.session()
    check_url = "https://energy.tv.weibo.cn/aj/checkspt?suid=5644764907&eid=10302"
    energy_url = "https://energy.tv.weibo.cn/aj/incrspt"
    for i in range(0, len(login_account_cookies.account_cookies)-1):
        headers = {
            "Host": "energy.tv.weibo.cn",
            "Referer": "https://energy.tv.weibo.cn/e/10302/index",
            "Cookie": login_account_cookies.account_cookies[i]
        }
        post_headers = {
            "Host": "energy.tv.weibo.cn",
            "Referer": "https://energy.tv.weibo.cn/e/10302/index?from=1110005030&wm=5399_0013&weiboauthoruid=3921596075&showurl=https%3A%2F%2Fenergy.tv.weibo.cn%2Fe%2F10302%2Findex%3Ffrom%3D1110005030%26wm%3D5399_0013%26weiboauthoruid%3D3921596075&url_open_direct=1&toolbar_hidden=1&containerid=231114_10302_tvenergy&luicode=10000011&lfid=1076033921596075",
            "Cookie": login_account_cookies.account_cookies[i]
        }
        check_card_res_json = json.loads(session.get(check_url, headers=headers).text)
        print(check_card_res_json)
        post_data = {
            "eid": "10302",
            "suid": "5644764907",
            "spt": "1",
            "send_wb": "1",
            "send_text": "生而为赢，不惧挑战！@火箭少女101_杨超越 我在#超新星全运会#加油能量榜上为你送出加油卡",
            "follow_uid": "2110705772",
            "page_type": "tvenergy_index_star"
        }
        energy_send_res = session.post(energy_url, data=post_data, headers=post_headers)
        energy_send_res_json = json.loads(energy_send_res.text)
        print(energy_send_res_json)