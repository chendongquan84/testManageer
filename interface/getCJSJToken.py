#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: dongquan
'''
from CJSJ import user
import web
render = web.template.render('templates/')

class getToken:
    def GET(self):
        return render.getCJSJToken()
    
class CJSJToken:
    def GET(self):
        i = web.input(phone=None)
        return user.user(i.phone).token
    
