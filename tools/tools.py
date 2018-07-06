#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月26日

@author: chendq
'''

import web
import myloger
import logging
from other import fileManger
# from other.upload import *
import tools
import json

# from function import courierDecrypt

from function.makeCardId import makeIDCardNo
# from function import courierDecrypt



class Tools:
    def GET(self,toolsName):
        return self.run(toolsName)
    def POST(self):
        '''{'toolsName':'makeIDCardNo'}'''
        data = web.data()
        data = json.loads(data)
        return json.dumps()
    
    def run(self,toolsName):
        if toolsName == 'makeIDCardNo':
            return makeIDCardNo()
        
class CourierDecrypt:
    def GET(self):
        str = web.input().str
	try:
            return courierDecrypt.decrypt(str)
	except:
	    return "不能转换，请确认输入正确"
    

    

