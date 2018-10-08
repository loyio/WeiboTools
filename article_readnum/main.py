# -*- coding: utf-8 -*-
"""
Created on 2018/10/8 

@author: susmote
"""


import requests
import time


if __name__ == '__main__':
    session = requests.session();
    while(True):
        atc_content = session.get("https://media.weibo.cn/article?id=2309404292838102854976").text
        print(atc_content[atc_content.find("read_count"):atc_content.find("read_count")+22])
        time.sleep(1)