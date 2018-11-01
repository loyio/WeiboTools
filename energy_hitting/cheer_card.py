# -*- coding: utf-8 -*-
"""
Created on 2018/10/30 

@author: susmote
"""

import requests
import json
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))
import login_account_cookies
print("批量微博加油卡系统".center(30, "*"))

if __name__ == '__main__':
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    if (len(sys.argv) < 2):
        print("请加上微博组号")
    else:
        if sys.argv[1] == "1":
            account_cookies = login_account_cookies.account_cookies_1
        elif sys.argv[1] == "2":
            account_cookies = login_account_cookies.account_cookies_2
        else:
            account_cookies = []
            print("没有这组号")
            exit()
        session = requests.session()
        check_url = "https://energy.tv.weibo.cn/aj/checkspt?suid=5644764907&eid=10302"
        energy_url = "https://energy.tv.weibo.cn/aj/incrspt"
        for i in range(0, len(account_cookies)):
            headers = {
                "Host": "energy.tv.weibo.cn",
                "Referer": "https://energy.tv.weibo.cn/e/10302/index",
                "Cookie": account_cookies[i]
            }
            post_headers = {
                "Host": "energy.tv.weibo.cn",
                "Referer": "https://energy.tv.weibo.cn/e/10302/index",
                "Cookie": account_cookies[i]
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
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("共花费%d秒" % (end_time - begin_time))