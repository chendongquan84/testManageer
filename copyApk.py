#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年12月16日

@author: chendq
'''

import shutil 
import os
import sys

from other import fileManger
from other import del_old_file
#import time

version = '1.0.0'
version = sys.argv[2]
workerDir = '/home/server/software/testManageer'
apkType = 'android-test'
apkType = sys.argv[1]
#apkType = 'android-simulation'
#apkType = 'android-release'
jekinsApk = '/home/tools/installed/jenkins/workspace/cjsj-app/seal/build/outputs/apk/成交设计云平台Wan1.3.15.apk'

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

del_old_file.del_old_file(versionDir,5)
