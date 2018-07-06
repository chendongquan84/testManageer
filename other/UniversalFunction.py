#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-7-10

@author: chendq
'''
import re
import os

def GetNoRepeatToList(list,Element):
    ''' 向列表中添加列表中不纯在的元素'''
    if Element in list:
        pass
    else:
        list.append(Element)
    return list

def regularFind(regular,str):
    '''检查并找出字符串中存在与指定正则匹配的字符串'''
    reg = re.compile(regular)
    match=reg.search(str)
    
    if match:
        if '(' in regular:
            return match.group(1)
        else:
            return match.group()
    else:
        return False
def fileFind(regular,path):
    '''查找指定路径下的符合指定格式文件名的所有文件'''
    files = []
    pathFiles = os.listdir(path)
    for file in pathFiles:
        if regularFind(regular,file):
            files.append(file)
    return files
def search(regular,string):
    reg = re.compile(regular)
    x = reg.findall(string)
    return x

def ReadConfig(configName):
    '''读取配置文件，获得字典格式的数据
       configName未配置文件名称,'''
    f = open(configName,"r")
    fd = f.readlines()
    f.close()
    rd = {}
    for line in fd:
        if '#' not in line and '=' in line:
            temp = [x.strip() for x in line.split("=")]
            key = temp[0]
            rd[key]=temp[1]
    return rd
if __name__ == '__main__':
    print regularFind('(\d*)-\d*.apk','android-test-2.4.1-0-0113151919.apk')
    
    
   
