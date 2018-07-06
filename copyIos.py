#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年12月16日

@author: chendq
'''

from other import fileManger
import shutil 
import os
from other import parseIpa
from other.UniversalFunction import *

def copyIos():
    #import time
    workerDir = '/home/test/testManageer'
    iosDir = 'files/iosClient'
    iosName = fileManger.getApkName(iosDir)
    iosPath = '/'.join([workerDir,iosDir,iosName])
    version = parseIpa.IPA(iosPath).bundle_version
    # print version 
         
    print iosName 
    iosType = regularFind('(.*).ipa',iosName) # 'rrkd-test'
    print iosType
    newDir = '/'.join([workerDir,'static/iosFiles/new'])
    
    oldName = fileManger.getApkName(newDir)  
    newIosName = fileManger.getNewApkName(iosType,version,oldName) + '.ipa'
    newIosPath = '/'.join([newDir,newIosName])
    fileManger.clearDir(newDir)
    # # 复制最新包到 temp
    shutil.copy2(iosPath,newIosPath)
    # # 清空version目录
    versionDir = '/'.join([workerDir,'static/iosFiles',version])
    print versionDir
    if os.path.exists(versionDir) :
        pass
    else:
        os.mkdir(versionDir)
    # 复制新apk到对应版本文件夹中
    shutil.copy2(newIosPath,versionDir)
    print 'copy ok'

