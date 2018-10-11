# -*- coding: utf-8 -*-
"""
Created on 2018/10/8 

@author: susmote
"""


import requests
import sys
import time

read_num_cmp = ''

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("请在后面加上头条文章链接")
    else:
        while(True):
            session = requests.session()
            atc_content = session.get(sys.argv[1]).text
            read_num = atc_content[atc_content.find("read_count"):atc_content.find("read_count")+23]
            if(read_num == read_num_cmp):
                print("已被官方限制，暂停阅读量更新")
                quit(0)
            else:
                read_num_cmp = read_num
                print(read_num_cmp)
            time.sleep(1)
