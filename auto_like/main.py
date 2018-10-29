# -*- coding: utf-8 -*-
"""
Created on 2018/10/29 

@author: susmote
"""

import requests
import sys
import os
sys.path.append(os.path.dirname(__file__))
import login_account


if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("请在后面加上你要点赞的微博链接")
    else:
        like_id = int(sys.argv[1][-16:len(sys.argv[1])])
        session = requests.session()
        like_url = "https://api.weibo.cn/2/like/set_like?new_version=0&gsid="+login_account.user_account[1]["gsid"]+"&wm=90163_90001&from=1885396040&c=weixinminiprogram&s="+login_account.user_account[1]["s"]
        postdata = {
            "id": like_id,
            "mid": like_id
        }
        res = session.post(like_url, data=postdata)
        print(res.text)