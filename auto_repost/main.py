# -*- coding: utf-8 -*-
"""
Created on 2018/11/4 

@author: susmote
"""
import requests
import json
import random
import time

rainbow_word_list = ["😀","😁","🤣","😂","😅","😆","😇","😉","😘","😙","😜","😝","😎","🤗"]

def auto_repost_func(weibolink, repostTopic, account_group, each_repost_count, printToGui , conn):
    """
    自动转发系统
    :param weibolink: 微博链接
    :param account_group: 号组
    :param each_comment_count: 单号转发次数
    :param outputTextEdit: 输出系统
    :return:
    """
    printToGui("微博自动转发")
    next_rannum = 20
    repost_count = 1
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    printToGui(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    account_index = 0
    while(True):
        session = requests.session()
        headers = {
            "Host": "m.weibo.cn",
            "Referer": "https://m.weibo.cn/compose/repost",
            "Cookie": account_group[account_index]
        }
        random_num = random.randint(0, len(rainbow_word_list) - 1)
        if(random_num != next_rannum):
            next_rannum = random_num
            repost_content = rainbow_word_list[next_rannum]+repostTopic
            repost_id = int(weibolink[-16:len(weibolink)])
            repost_url = "https://m.weibo.cn/api/statuses/repost"
            st_url = "https://m.weibo.cn/api/config"
            login_data = session.get(st_url, headers=headers).text
            login_data_json = json.loads(login_data)["data"]
            postdata = {
                "id": repost_id,
                "content": repost_content,
                "mid": repost_id,
                "st":login_data_json["st"]
            }
            res = session.post(repost_url, data=postdata, headers=headers)
            if res.text != "File not found.\n":
                print("".center(30, "*"))
                printToGui(str("".center(30, "*")))
                print("账号id " + str(account_index + 1))
                printToGui("账号id " + str(account_index + 1))
                res_json = json.loads(res.text)
                if res_json["ok"] == 0:
                    print(res_json)
                    printToGui(str(res_json))
                    if res_json["errno"] == "20003" or res_json["errno"] == "20034":
                        c = conn.cursor()
                        update_cmd = "UPDATE WeiboCookies SET STATE=\'号已被封禁,需要手机验证解封\' WHERE \"COOKIES\" = " + "\"" + account_group[account_index] + "\""
                        c.execute(update_cmd)
                        conn.commit()
                        printToGui(res_json["msg"])
                if account_index == len(account_group)-1:
                    print("第" + str(repost_count) + "轮结束")
                    printToGui("第" + str(repost_count) + "轮结束")
                    repost_count += 1
                    account_index = 0
                    time.sleep(20)
                    continue
                if repost_count == each_repost_count+1:
                    end_time = time.time()
                    print("转发结束")
                    printToGui("转发全部结束")
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    printToGui(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    spend_time = end_time - begin_time
                    print("共花费" + str(spend_time) + "秒")
                    printToGui("共花费" + str(spend_time) + "秒")
                    return 0
                else:
                    account_index += 1
                    continue
            else:
                print("账号id "+str(account_index + 1)+" 此号未绑定")
                printToGui("账号id "+str(account_index + 1)+"此号未绑定")
                print("".center(30, "*"))
                printToGui(str("".center(30, "*")))
                if account_index == len(account_group):
                    print("第" + str(repost_count + 1) + "轮结束")
                    printToGui("第" + str(repost_count + 1) + "轮结束")
                    time.sleep(20)
                    repost_count += 1
                    account_index = 0
                    continue
                if repost_count == each_repost_count+1:
                    end_time = time.time()
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    printToGui(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    spend_time = end_time - begin_time
                    print("共花费" + str(spend_time) + "秒")
                    printToGui("共花费" + str(spend_time) + "秒")
                    return 0
                else:
                    account_index += 1
                    continue
        else:
            continue





def auto_repost_test_func(weibolink,  account_group, each_repost_count, printToGui , conn):
    """
    自动转发系统
    :param weibolink: 微博链接
    :param account_group: 号组
    :param each_comment_count: 单号转发次数
    :param outputTextEdit: 输出系统
    :return:
    """
    printToGui("微博自动转发")
    next_rannum = 20
    repost_count = 0
    take_count = 0
    begin_time = time.time()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    printToGui(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    account_index = 0
    while(True):
        session = requests.session()
        headers = {
            "Host": "m.weibo.cn",
            "Referer": "https://m.weibo.cn/compose/repost",
            "Cookie": account_group[account_index]
        }
        random_num = random.randint(0, len(rainbow_word_list) - 1)
        if(random_num != next_rannum):
            repost_count += 1
            next_rannum = random_num
            repost_content = rainbow_word_list[next_rannum]
            repost_id = int(weibolink[-16:len(weibolink)])
            repost_url = "https://m.weibo.cn/api/statuses/repost"
            st_url = "https://m.weibo.cn/api/config"
            login_data = session.get(st_url, headers=headers).text
            login_data_json = json.loads(login_data)["data"]
            postdata = {
                "id": repost_id,
                "content": repost_content,
                "mid": repost_id,
                "st":login_data_json["st"]
            }
            res = session.post(repost_url, data=postdata, headers=headers)
            if res.text != "File not found.\n":
                res_json = json.loads(res.text)
                if res_json["ok"] == 0 or repost_count == each_repost_count:
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
