# -*- coding: utf-8 -*-
"""
Created on 2018/10/30 

@author: susmote
"""

import requests
import json
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))
import login_account_cookies

print("评论点赞系统".center(30, "*"))

if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print("请加上微博链接和微博组号")
    else:
        begin_time = time.time()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        if sys.argv[2] == "1":
            account_cookies = login_account_cookies.account_cookies_1
        elif sys.argv[2] == "2":
            account_cookies = login_account_cookies.account_cookies_2
        elif sys.argv[2] == "3":
            account_cookies = login_account_cookies.account_cookies_3
        else:
            account_cookies = []
            print("没有这组号")
            exit()
        session = requests.session()
        weibo_id = sys.argv[1][-16:len(sys.argv[1])]
        weibo_url = "https://m.weibo.cn/comments/hotflow?id="+ weibo_id +"&mid="+ weibo_id +"&max_id_type=0"
        res_comment = session.get(weibo_url)
        res_comment_json = json.loads(res_comment.text)["data"]["data"]
        for i in range(0, len(res_comment_json)):
            print("评论id:", res_comment_json[i]["id"], "评论者:", res_comment_json[i]["user"]["screen_name"], "评论内容:", res_comment_json[i]["text"], "点赞数: ", res_comment_json[i]["like_count"])
        comment_id = int(input("请输入你要进行点赞的评论id: "))
        comment_like_url = "https://m.weibo.cn/api/likes/update"
        for i in range(0, len(account_cookies)):
            headers = {
                "Host": "m.weibo.cn",
                "Cookie": account_cookies[i]
            }
            st_url = "https://m.weibo.cn/api/config"
            login_data = session.get(st_url, headers=headers).text
            login_data_json = json.loads(login_data)["data"]
            post_data = {
                "id":comment_id,
                "type":"comment",
                "st":login_data_json["st"]
            }
            like_session = requests.session()
            cmt_like_res = like_session.post(comment_like_url, data=post_data, headers=headers)
            cmt_like_res_json = json.loads(cmt_like_res.text)
            if cmt_like_res_json["ok"] == 1:
                print("点赞成功")
            else:
                print(i, cmt_like_res_json["msg"])
        end_time = time.time()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print("共花费%d秒" % (end_time - begin_time))
