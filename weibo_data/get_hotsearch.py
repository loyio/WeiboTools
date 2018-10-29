# -*- coding: utf-8 -*-
"""
Created on 2018/10/29 

@author: susmote
"""

import requests
import string
import json


if __name__ == '__main__':
    session = requests.session()
    gsid = "_2A_p6S-ysCoX0ky4qkg3cQ1QN3MHlPcwoRnlmzmFeEtLG8oFeQ6sxWFSEZN4d2FZLZYN_tpY_eTM9CYIIYlEybHdp"
    user_link = "https://api.weibo.cn/2/page?gsid="+ gsid +"&from=1885396040&wm=90163_90001&c=weixinminiprogram&s=8024905d&lang=zh_CN&containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&count=20"
    raw_user_info = session.get(user_link).text
    user_info_json = json.loads(raw_user_info)
    print(user_info_json["pageInfo"]["title_top"])
    hotsearch_card = user_info_json["cards"][0]["card_group"]
    print("排名\t搜索词\t搜索量")
    for hs_item_count in range(1, len(hotsearch_card)):
        print(hs_item_count, "\t", hotsearch_card[hs_item_count]["desc"].rjust(18), "\t", hotsearch_card[hs_item_count]["desc_extr"])
