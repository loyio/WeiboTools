# -*- coding: utf-8 -*-
"""
Created on 2018/10/30 

@author: susmote
"""


import requests
import json
import time

def auto_post_weibo(account_cookies, weibo_content, printToGui, conn):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    begin_time = time.time()
    for i in range(0, len(account_cookies)):
        session = requests.session()
        post_weibo_url = "https://m.weibo.cn/api/statuses/update"
        headers = {
            "Referer": "https://m.weibo.cn",
            "Cookie": account_cookies[i]
        }
        st_url = "https://m.weibo.cn/api/config"
        login_data = session.get(st_url, headers=headers).text
        login_data_json = json.loads(login_data)["data"]
        print(login_data_json)
        printToGui(str(login_data_json))
        post_data = {
            "content": weibo_content,
            "st": login_data_json["st"]
        }
        post_weibo_res = session.post(post_weibo_url, data=post_data, headers=headers)
        post_weibo_res_json = json.loads(post_weibo_res.text)
        if post_weibo_res_json["ok"] == 1:
            print(i+1,"发微博成功")
            printToGui(str(i+1)+" 发微博成功")
        else:
            print(i+1,post_weibo_res_json["msg"])
            printToGui(str(i+1)+post_weibo_res_json["msg"])
            if post_weibo_res_json["errno"] == "20003":
                c = conn.cursor()
                delete_cmd = "DELETE FROM WeiboCookies WHERE \"COOKIES\" = " + "\"" + account_cookies[i] + "\""
                c.execute(delete_cmd)
                conn.commit()
                printToGui(post_weibo_res_json["msg"])
    end_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print("共花费%d秒"%(end_time - begin_time))
    spend_time = end_time - begin_time
    printToGui("共花费"+str(spend_time)+"秒")