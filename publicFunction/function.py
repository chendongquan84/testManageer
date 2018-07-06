#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年11月2日

@author: chendq
'''
import hashlib
#import base64
#import json


def getMd5(str): 
    m  = hashlib.md5(str)
    pws = m.hexdigest()
    return pws

def update_dict(myDict,str):
    myList = [lists for lists in str.split(',')]
    for list in myList:
        temp = [t.strip() for t in list.split('=')]
        myDict[temp[0]] = temp[1]
    return myDict






