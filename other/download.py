#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年2月24日

@author: chendq
'''

import requests
import StringIO

def download(requestsUrl,saveFileName): 
    '''下载文件：
        requestsUrl为下载url，saveFileName为保存文件路径及文件名
        e.g.:
        download('http://www.baidu.com/baidu.img','./download.png')
        --> <type 'instance'>
            200'''
    try:
        req = requests.get(requestsUrl,timeout=30)
        file_name =saveFileName
        binary_file = req.content
        f= StringIO.StringIO(binary_file)
        print(type(f))
        a= dir(req.raw)
        f= open(file_name,'wb')
        f.write(binary_file)
        f.close()
        print(req.status_code)
    except Exception as error:
        print(str(error))