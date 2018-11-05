# -*- coding: utf-8 -*-
"""
Created on 2018/11/4 

@author: susmote
"""
import requests
import json
import random
import time


def auto_like(weibolink,  account_group, printToGui , conn):
    """
    自动点赞系统
    :param weibolink: 微博链接
    :param account_group: 号组
    :param outputTextEdit: 输出系统
    :return:
    """
    printToGui("微博批量自动点赞")
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    printToGui(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    account_index = 0
    while(True):
        session = requests.session()
        headers = {
            "Host": "m.weibo.cn",
            "Referer": "https://m.weibo.cn/",
            "Cookie": account_group[account_index]
        }
        like_id = int(weibolink[-16:len(weibolink)])
        like_url = "https://m.weibo.cn/api/attitudes/create"
        st_url = "https://m.weibo.cn/api/config"
        login_data = session.get(st_url, headers=headers).text
        login_data_json = json.loads(login_data)["data"]
        postdata = {
            "id": like_id,
            "attitude": "heart",
            "st":login_data_json["st"]
        }
        res = session.post(like_url, data=postdata, headers=headers)
        if res.text != "File not found.\n":
            res_json = json.loads(res.text)
            print("".center(30, "*"))
            printToGui(str("".center(30, "*")))
            print("账号id " + str(account_index + 1))
            printToGui("账号id " + str(account_index + 1))
            if res_json["ok"] == 0:
                print("点赞失败")
                printToGui("点赞失败")
                print(res_json)
                printToGui(str(res_json))
                if res_json["errno"] == "20003" or res_json["errno"] == "20034":
                    c = conn.cursor()
                    delete_cmd = "DELETE FROM WeiboCookies WHERE \"COOKIES\" = " + "\"" + account_group[account_index] + "\""
                    c.execute(delete_cmd)
                    conn.commit()
                    printToGui(res_json["msg"])
            else:
                print("点赞成功")
                printToGui("点赞成功")
                account_index+=1
                if account_index == len(account_group):
                    print("点赞结束")
                    printToGui("点赞结束")
                    end_time = time.time()
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    printToGui(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    spend_time = end_time - begin_time
                    print("共花费"+ str(spend_time) +"秒")
                    printToGui("共花费"+ str(spend_time) +"秒")
                    return 0
        else:
            print("账号id "+str(account_index + 1)+" 此号未绑定")
            printToGui("账号id "+str(account_index + 1)+"此号未绑定")
            print("".center(30, "*"))
            printToGui(str("".center(30, "*")))
            account_index += 1
            if account_index == len(account_group):
                print("点赞结束")
                printToGui("点赞结束")
                end_time = time.time()
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                printToGui(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                spend_time = end_time - begin_time
                print("共花费" + str(spend_time) + "秒")
                printToGui("共花费" + str(spend_time) + "秒")
            return 0
