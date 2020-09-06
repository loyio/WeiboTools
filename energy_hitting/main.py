# -*- coding: utf-8 -*-
"""
Created on 2018/11/4 

@author: susmote
"""

import requests
import json
import time

def post_weibo(account_cookies, printToGui):
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    printToGui(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
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
            "content": "@XXX 我在#超新星全运会#为你加油！生而为赢，不惧挑战！ http://t.cn/EzV5piM",
            "st": login_data_json["st"]
        }
        post_weibo_res = session.post(post_weibo_url, data=post_data, headers=headers)
        post_weibo_res_json = json.loads(post_weibo_res.text)
        if post_weibo_res_json["ok"] == 1:
            print(i+1," 发微博成功")
            printToGui(str(i+1)+" 发微博成功")
        else:
            print(i+1,post_weibo_res_json["msg"])
            printToGui(str(i+1)+post_weibo_res_json['msg'])
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    printToGui(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    spend_time = end_time - begin_time
    print("共花费%d秒"%(spend_time))
    printToGui("共花费" + str(spend_time) + "秒")


def repost_weibo(account_cookies, printToGui):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    printToGui(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    begin_time = time.time()
    for i in range(0, len(account_cookies)):
        session = requests.session()
        post_weibo_url = "https://energy.tv.weibo.cn/aj/repost"
        headers = {
            "Referer": "https://energy.tv.weibo.cn/aj/repost?eid=10302&suid=5644764907&page_type=tvenergy_index_star",
            "Cookie": account_cookies[i]
        }
        post_data = {
            "mid": "4301539303030712",
            "text": "@### 我在#超新星全运会#为你加油！生而为赢，不惧挑战！",
            "follow": "5644764907",
            "eid": "10302",
            "suid": "5644764907",
            "page_type": "tvenergy_index_star"
        }
        repost_weibo_res = session.post(post_weibo_url, data=post_data, headers=headers)
        try:
            repost_weibo_res_json = json.loads(repost_weibo_res.text)
            if repost_weibo_res_json["code"] == "100000":
                print(i+1,"转发微博成功 ", repost_weibo_res_json["msg"])
                printToGui(str(i+1)+" 转发微博成功 "+repost_weibo_res_json["msg"])
            else:
                print(i+1,repost_weibo_res_json["msg"])
                printToGui(str(i+1)+repost_weibo_res_json["msg"])
        except Exception as e:
            printToGui(str(e))
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    printToGui(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    spend_time = end_time - begin_time
    print("共花费%d秒"%(spend_time))
    printToGui("共花费"+str(spend_time)+"秒")


def cheer_card(account_cookies, printToGui):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    printToGui(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    begin_time = time.time()
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
        check_card_res = session.get(check_url, headers=headers)
        print(check_card_res.text)
        check_card_res_json = json.loads(check_card_res.text)
        print(check_card_res_json)
        printToGui(str(check_card_res_json))
        post_data = {
            "eid": "10302",
            "suid": "5644764907",
            "spt": 1,
            "send_wb": "1",
            "send_text": "生而为赢，不惧挑战！@XXX 我在#超新星全运会#加油能量榜上为你送出加油卡",
            "follow_uid": "2110705772",
            "page_type": "tvenergy_index_star"
        }
        energy_send_res = session.post(energy_url, data=post_data, headers=post_headers)
        energy_send_res_json = json.loads(energy_send_res.text)
        print(energy_send_res_json)
        printToGui(str(energy_send_res_json))
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    printToGui(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    spend_time = end_time - begin_time
    print("共花费%d秒" % (spend_time))
    printToGui("共花费" + str(spend_time) + "秒")
