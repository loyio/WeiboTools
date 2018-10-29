# -*- coding: utf-8 -*-
"""
Created on 2018/10/29 

@author: susmote
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))
import data

print(data.name)

count = 0
while(True):
    print(count)
    count+=1
    if count == 20:
        exit()
    else:
        continue
