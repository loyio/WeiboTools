# -*- coding: utf-8 -*-
"""
Created on 2018/10/29 

@author: loyio
"""
import requests
import json
import random
import time
import sys
import os
import sqlite3
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))

rainbow_word_list = ["word_test"]

def auto_comment_func(weibolink,  account_group, each_comment_count, printToGui , conn):
    """
    自动评论系统
    :param weibolink: 微博链接
    :param account_group: 号组
    :param each_comment_count: 单号评论次数
    :param outputTextEdit: 输出系统
    :return:
    """
    printToGui("微博自动评论系统")
    next_rannum = 20
    comment_count = 0
    take_count = 0
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    printToGui(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    account_index = 0
    while(True):
        session = requests.session()
        headers = {
            "Host": "m.weibo.cn",
            "Cookie": account_group[account_index]
        }
        random_num = random.randint(0, len(rainbow_word_list) - 1)
        if(random_num != next_rannum):
            comment_count += 1
            next_rannum = random_num
            comment_content = rainbow_word_list[next_rannum]
            comment_id = int(weibolink[-16:len(weibolink)])
            comment_url = "https://m.weibo.cn/api/comments/create"
            st_url = "https://m.weibo.cn/api/config"
            login_data = session.get(st_url, headers=headers).text
            login_data_json = json.loads(login_data)["data"]
            postdata = {
                "content": comment_content,
                "mid": comment_id,
                "st":login_data_json["st"]
            }
            res = session.post(comment_url, data=postdata, headers=headers)
            if res.text != "File not found.\n":
                res_json = json.loads(res.text)
                if res_json["ok"] == 0 or comment_count == each_comment_count:
                    print("".center(30, "*"))
                    printToGui(str("".center(30, "*")))
                    print("账号id " + str(account_index + 1))
                    printToGui("账号id " + str(account_index + 1))
                    if res_json["ok"] == 0:
                        print(res_json)
                        printToGui(str(res_json))
                        if res_json["errno"] == "20003" or res_json["errno"] == "20034":
                            c = conn.cursor()
                            delete_cmd = "DELETE FROM WeiboCookies WHERE \"COOKIES\" = " + "\"" + account_group[account_index] + "\""
                            c.execute(delete_cmd)
                            conn.commit()
                            printToGui(res_json["msg"])
                    comment_count = 0
                    account_index+=1
                    if account_index == len(account_group):
                        print("第" + str(take_count+1) + "轮结束")
                        printToGui("第" + str(take_count+1) + "轮结束")
                        end_time = time.time()
                        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                        printToGui(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                        spend_time = end_time - begin_time
                        print("共花费"+ str(spend_time) +"秒")
                        printToGui("共花费"+ str(spend_time) +"秒")
                        take_count += 1
                        return 0
                    else:
                        continue
                else:
                    continue
            else:
                print("账号id "+str(account_index + 1)+" 此号未绑定")
                printToGui("账号id "+str(account_index + 1)+"此号未绑定")
                print("".center(30, "*"))
                printToGui(str("".center(30, "*")))
                account_index += 1
                if account_index == len(account_group):
                    print("第" + str(take_count + 1) + "轮结束")
                    printToGui("第" + str(take_count + 1) + "轮结束")
                    end_time = time.time()
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    printToGui(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    spend_time = end_time - begin_time
                    print("共花费" + str(spend_time) + "秒")
                    printToGui("共花费" + str(spend_time) + "秒")
                    take_count += 1
                    return 0
        else:
            continue

