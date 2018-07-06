#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月26日

@author: chendq
'''
import random
import time

def makeIDCardNo():
    '''随机生成新的18位身份证号码 '''
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                        random.randint(01,99),
                                        random.randint(01,99),
                                        random.randint(t - 55, t - 18), # 设置年阶段
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(1,999))
    y = 0
    for i in range(17):
            y += int(x[i]) * ARR[i]
    
    return '%s%s' %(x, LAST[y % 11])