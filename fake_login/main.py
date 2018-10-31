# -*- coding: utf-8 -*-
"""
Created on 2018/10/31 

@author: susmote
"""

import requests


if __name__ == '__main__':
    session = requests.session()
    login_url = "https://passport.weibo.cn/signin/login"
    login_page_data = {
        "entry": "mweibo",
        "res": "wel",
        "wm": "3349",
        "r": "https://m.weibo.cn/"
    }
    login_page_res = session.get(login_url, data=login_page_data)
    print(login_page_res.text)