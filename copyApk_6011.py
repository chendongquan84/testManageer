#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年12月16日

@author: chendq
'''

from other import fileManger
import shutil 
import os
import sys
#import time

version = '2.6.2'
version = sys.argv[2]
workerDir = '/home/test/testManageer'
apkType = 'android-test'
apkType = sys.argv[1]
#apkType = 'android-simulation'
#apkType = 'android-release'
jekinsApk = '/home/jenkins_home/jobs/Android_test_60.11/workspace/app/build/outputs/apk/app-rrkd-release.apk'

# 清空new目录
newDir = '/'.join([workerDir,'static/apkFiles/new'])
oldName = fileManger.getApkName(newDir)
print 'oldName',oldName
newApkName = fileManger.getNewApkName(apkType,version,oldName) + '.apk'
newApkPath = '/'.join([newDir,newApkName])
fileManger.clearDir(newDir)
# # 复制最新包到 temp
shutil.copy2(jekinsApk,newApkPath)
# # 清空version目录
versionDir = '/'.join([workerDir,'static/apkFiles',version])
if os.path.exists(versionDir) :
    pass
else:
    os.mkdir(versionDir)
    # 复制新apk到对应版本文件夹中
shutil.copy2(newApkPath,versionDir)


