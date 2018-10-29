# -*- coding: utf-8 -*-
"""
Created on 2018/10/28 

@author: susmote
"""

import requests
import sys
import json


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("请在后面加上微博用户名")
    else:
        session = requests.session()
        user_link = "https://api.weibo.cn/2/profile?new_version=0&user_domain=n/" + sys.argv[1]
        raw_user_info = session.get(user_link).text
        user_info_json = json.loads(raw_user_info)["userInfo"]
        print("微博用户名: ", user_info_json["name"])
        if(user_info_json["verified"] == True):
           print("微博认证  : ", user_info_json["verified_reason"])
        print("微博粉丝数: ", user_info_json["followers_count"])