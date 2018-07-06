#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月25日

@author: chendq
'''

import web
#import myloger
import logging
import tools
import json

class randomCoordinates:
    def POST(self):
        logging.info('start')
        data = web.data()
        data = json.loads(data)
        logging.info(data)
        return json.dumps(tools.makeCoorDinate(data['city'], data['address'], data['r']))
    def GET(self,city,address,r):
        r = float(r)
        data = tools.makeCoorDinate(city,address,r)
        return data