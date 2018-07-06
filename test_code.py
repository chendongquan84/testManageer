#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年12月16日

@author: chendq
'''
import web
import myloger
import logging
from other import fileManger
from other.upload import *


if __name__ == '__main__':
    #copyIos('./files', './static/iosFiles/new/')
    apkType = 'android_test'
    version = '2.3.9'
    oldApkName = 'android-test-parseIpa9-12-23423432423.apk'
    print fileManager.getNewApkName(apkType,version,oldApkName)
