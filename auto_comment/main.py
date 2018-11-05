# -*- coding: utf-8 -*-
"""
Created on 2018/10/29 

@author: susmote
"""
import requests
import json
import random
import time
import sys
import os
import sqlite3
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))

rainbow_word_list = ["必须支持杨超越[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "杨超越美爆了。 正妹[爱你][爱你][爱你][爱你]  我的妹妹就是美[爱你][爱你][爱你]  母爱变质的一天[爱你][爱你][爱你][爱你]  今天是女友粉[爱你][爱你][爱你][爱你]    想把她藏起来！可是不可以[爱你][爱你][爱你][爱你]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "越来越美 越看越美 特别吃超越的颜啊 希望以后能够有更多机会成长 我知道善良又宠粉你没有让我们失望 你是我心中的No.1 你越来越好越来越快乐 天天开心[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "妹妹除了一如既往地美丽与帅气外，月芽儿们正在见证超越的成长与进步。满满的正能量！一起加油吧。[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "我爱的人啊，她有世上最好看的侧颜和最温柔的眼睛还有最好听的名字。[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "喜欢可爱的你，充满元气，无知无畏勇往直前，会流泪却不会放弃倒下的小可爱，今天有超越自己吗？@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "帅爆杨超越🤵，了解一下可盐可甜的钢铁直男神颜少女[允悲][允悲][允悲]这些词搭配起来真的是有够奇怪，但说的就是杨超越[心][心][心]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "表白我小可爱噼里啪啦爆炸无敌顶天立地钢铁直男杨超越！！！！@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "ycy今日份美颜已在我心里收藏[羞嗒嗒][羞嗒嗒][羞嗒嗒]加油。@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "必须支持杨超越[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越射箭#",
                "我最近有点低血糖。”  “好像是因为太久没见你了。”[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "杨超越你去学游泳吧，这样我们就能永浴爱河了﻿﻿💋@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "恰好你有我喜欢所有的样子！喜欢超越[好喜欢][好喜欢][好喜欢]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "有生之年，欣喜相逢。你就是我的天使。[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#",
                "一时失语，这样自然精致豪无攻击的面容😘，超超越越加油！！[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越 #杨超越超新星全运会# #杨超越 射箭#"]

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

