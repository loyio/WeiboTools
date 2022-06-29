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
sys.path.append(os.path.dirname(__file__))
import login_account

rainbow_word_list = ["test comment"]


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
