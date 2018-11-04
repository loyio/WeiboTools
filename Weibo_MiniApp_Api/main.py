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
sys.path.append(os.path.dirname(__file__))
import login_account

rainbow_word_list = ["#正能量偶像杨超越#必须支持杨超越[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越",
                "杨超越美爆了。 正妹[爱你][爱你][爱你][爱你]  我的妹妹就是美[爱你][爱你][爱你]  母爱变质的一天[爱你][爱你][爱你][爱你]  今天是女友粉[爱你][爱你][爱你][爱你]    想把她藏起来！可是不可以[爱你][爱你][爱你][爱你]@火箭少女101_杨超越 #正能量偶像杨超越#",
                "#正能量偶像杨超越#越来越美 越看越美 特别吃超越的颜啊 希望以后能够有更多机会成长 我知道善良又宠粉你没有让我们失望 你是我心中的No.1 你越来越好越来越快乐 天天开心[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越",
                "#正能量偶像杨超越#妹妹除了一如既往地美丽与帅气外，月芽儿们正在见证超越的成长与进步。满满的正能量！一起加油吧。[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越",
                "#正能量偶像杨超越#我爱的人啊，她有世上最好看的侧颜和最温柔的眼睛还有最好听的名字。[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越",
                "#正能量偶像杨超越#喜欢可爱的你，充满元气，无知无畏勇往直前，会流泪却不会放弃倒下的小可爱，今天有超越自己吗？@火箭少女101_杨超越",
                "#正能量偶像杨超越#帅爆杨超越🤵，了解一下可盐可甜的钢铁直男神颜少女[允悲][允悲][允悲]这些词搭配起来真的是有够奇怪，但说的就是杨超越[心][心][心]@火箭少女101_杨超越",
                "#正能量偶像杨超越#表白我小可爱噼里啪啦爆炸无敌顶天立地钢铁直男杨超越！！！！@火箭少女101_杨超越",
                "#正能量偶像杨超越#ycy今日份美颜已在我心里收藏[羞嗒嗒][羞嗒嗒][羞嗒嗒]加油。@火箭少女101_杨超越",
                "#正能量偶像杨超越#必须支持杨超越[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越",
                "#正能量偶像杨超越#“我最近有点低血糖。”  “好像是因为太久没见你了。”[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越",
                "#正能量偶像杨超越#杨超越你去学游泳吧，这样我们就能永浴爱河了﻿﻿💋@火箭少女101_杨超越",
                "#正能量偶像杨超越#恰好你有我喜欢所有的样子！喜欢超越[好喜欢][好喜欢][好喜欢]@火箭少女101_杨超越",
                "#正能量偶像杨超越#有生之年，欣喜相逢。你就是我的天使。[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越",
                "#正能量偶像杨超越#一时失语，这样自然精致豪无攻击的面容😘，超超越越加油！！[羞嗒嗒][羞嗒嗒][羞嗒嗒]@火箭少女101_杨超越"]


test_count = 0
next_rannum = 20
if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print("请在后面加上你要评论的微博链接和要进行评论的账号")
    else:
        while(True):
            test_count+=1
            print("评论次数",test_count)
            session = requests.session()
            random_num = random.randint(0, len(rainbow_word_list) - 1)
            if(random_num != next_rannum):
                next_rannum = random_num
                comment_content = rainbow_word_list[next_rannum]
                comment_id = int(sys.argv[2][-16:len(sys.argv[2])])
                comment_url = "https://api.weibo.cn/2/comments/create?gsid="+ login_account.user_account[int(sys.argv[1])]["gsid"] +"&from=1885396040&c=weixinminiprogram&s="+ login_account.user_account[int(sys.argv[1])]['s']
                postdata = {
                    "comment": comment_content,
                    "id": comment_id
                }
                res = session.post(comment_url, data=postdata)
                res_json = json.loads(res.text)
                if list(res_json.keys())[0] == "errmsg":
                    print(res_json["errmsg"])
                    time.sleep(360)
                    continue
                else:
                    continue
            else:
                continue