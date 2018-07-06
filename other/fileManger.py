#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年11月14日

@author: chendq
'''

import os
import qrcode
import time
import anydbm
host = 'http://182.254.213.25:8081'
import shutil 
import random 
from other import UniversalFunction

def makeQrcode(qrData,imgDir):
    qr = qrcode.QRCode(     
                       version=1,     
                       error_correction=qrcode.constants.ERROR_CORRECT_L,     
                       box_size=6,     
                       border=1, 
                       ) 
    
    qr.add_data(qrData)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(imgDir)
    return

def getVersionList(apkDir):
    list = os.listdir(apkDir)
    list.remove(list[-1])
    list.sort()
    list.reverse()
    return list
def getFileList(fileDir):
    try:
	list = os.listdir(fileDir)
	list.sort()
	list.reverse()
        return list
    except:
        return None

def getApkName(fileDir):
    try:
        return os.listdir(fileDir)[0]
    except:
        return 

def getImgName(apkName):
    fileName = apkName.split('.')[0]
    return fileName + '.png'

def getNewApkName_backup(apkName,num=-5):
    # apkname='login-2.20-2.apk'
    temp = list(apkName)
    try:
        temp[num] = str(int(temp[num]) + 1)
    except:
        print'原文件命名规则可能错误'
    return''.join(temp)
def formatNum(number):
    number = str(number)
    l = 3 - len(number)
    for x in range(l):
        number = '0' + str(number)
    return number

#def getNewApkName(apkType,version,oldApkName):
#    # oldApkName = android-test-parseIpa0-12-201434234324.apk
#    
#    apkType = apkType
#    version = version
#    if oldApkName:
#        oldVersion = UniversalFunction.regularFind('-(\d*\.\d*\.\d*)-\d*-\d*.apk',oldApkName)
#    else:
#	oldVersion = None
#    try:
#        if oldApkName and oldVersion == version:
#            number = int(UniversalFunction.regularFind('(\d*)-\d*.apk',oldApkName))
#        else:
#            number = 0
#        return '-'.join([apkType,version,formatNum(number + 1),time.strftime("%y%m%d%H%M%S", time.localtime())])
#    except Exception, e:
#        print e
def getNewApkName(apkType,version,oldApkName):
    return '-'.join([apkType,version,time.strftime("%y%m%d%H%M%S", time.localtime())])
def clearDir(path):
    names = os.listdir(path)
    for name in names:
        _path = '/'.join([path,name])
        if os.path.isfile(_path):
            try:
                os.remove(_path)
            except Exception, e:
                print e
        else:
            try:
                os.rmdir(_path)
            except Exception, e:
                print e
    return

def copyIos(dir,path):
    fileName = getFileList(dir)[0]
    print fileName
    if 'ipa' in fileName:
        shutil.copy2('/'.join([dir,fileName]), path)
        print 'copy %s to %s ok at %s' % (fileName,path,time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))
    return

def getTempFileName():
    name = '_'.join(['temp',time.strftime("%y%m%d%H%M%S", time.localtime()),str(random.randint(1000000,9999999))])
    return name
        

if __name__ == '__main__':
    #copyIos('./files', './static/iosFiles/new/')
    makeQrcode('test1231232123123','./test.jpg')
