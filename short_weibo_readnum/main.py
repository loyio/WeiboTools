# -*- coding: utf-8 -*-
"""
Created on 2018/10/8 

@author: susmote
"""


import requests
import time
from bs4 import BeautifulSoup


if __name__ == '__main__':
    session = requests.session()
    atc_content = session.get("https://www.weibo.com/loveycyue").text
    print(atc_content)
    time.sleep(1)
