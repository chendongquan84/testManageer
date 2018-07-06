#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年1月16日

@author: chendq
'''
import web
# import myloger
import logging
from other import fileManger
# from other.upload import *

# from tools.tools import CourierDecrypt

androidFileDir = 'static/apkFiles'
iosFileDir = 'static/iosFiles'
downUrl = 'http://192.168.0.213:8100'

class index:
    '''主页：最新安装包（ios，android）二维码展示'''
    def GET(self):
        newAndroidName = fileManger.getApkName('/'.join([androidFileDir,'new']))
        newIosName = fileManger.getApkName('/'.join([iosFileDir,'new']))
        try:
            apkDwonpath = '/'.join([androidFileDir,'new',newAndroidName])
        except:
            apkDwonpath = None
        try:
            iosDwonpath = '/'.join([iosFileDir,'new',newIosName])
        except:
            iosDwonpath = None
        return render.index(newAndroidName,newIosName,downUrl,apkDwonpath,iosDwonpath)
    def POST(self):
        data = web.data()
        logging.info(data)
        return 'success'
class android:
    def GET(self):
        androidVersion = fileManger.getFileList(androidFileDir)
        print androidVersion
        androidVersion.remove('new')
        if androidVersion:
            return render.android(androidVersion)
        else:
            return render.erro( '暂时还没有可下载android版本客户断')
class ios:
    def GET(self):
        iosVersion = fileManger.getFileList(iosFileDir)
        iosVersion.remove('new')
        if iosVersion:
            return render.ios(iosVersion)
        else:
            return render.erro( '暂时还没可下载ios版本客户端')
class androidVer:
    def GET(self,version):
        dir = '/'.join([androidFileDir,version])
        files = fileManger.getFileList(dir)
        if files:
            return render.fileDownList('/'.join([androidFileDir ,version]),files,downUrl)
        else:
            return render.erro('暂时还没有该版本客户端可下载')
class iosVer:
    def GET(self,version):
        dir = '/'.join([iosFileDir,version])
        files = fileManger.getFileList(dir)
        if files:
            return render.fileDownList('/'.join([iosFileDir ,version]),files,downUrl)
        else:
            return render.erro('暂时还没有该版本客户端可下载')
class makeQR:
    def GET(self):
        qrData = web.input().data
        imgDir = './static/img/tempimg.png'
        fileManger.makeQrcode(qrData, imgDir)
        return render.imgshow(qrData,imgDir)
#class DecryptWeb:
#    def GET(self):
#        return render.DecryptWeb()
        
# CourierDecrypt = CourierDecrypt

if __name__ == '__main__':
    
    urls = ("/", "index",
            "/android$","android",
            "/ios$","ios",
            "/android/ver/(.*\d)","androidVer",
            "/ios/ver/(.*\d)","iosVer",
            "/login/(.*)",'login',
            "/makeQR","makeQR",
#            "/tools/CourierDecrypt","CourierDecrypt",
#            "/tools/DecryptWeb","DecryptWeb"
		)
    
    render = web.template.render('templates/')
    app = web.application(urls, globals())
    response = app.request("/", https=True)
    app.run()
   
