#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年11月16日

@author: chendq
'''

 # python 2.7.5
# project need third_party lib biplist, please run 'sudo pip install biplist'

import zipfile
import biplist
import tempfile
import shutil
import re
import os


class IPA(object):

    def __init__(self, ipa_path):
        self.__ipapath = ipa_path
        self.__plist = None
    
    # CFBundleDisplayName
    @property
    def bundle_display_name(self):
        return self.plist.get('CFBundleDisplayName')
    
    # CFBundleName
    @property
    def bundle_name(self):
        return self.plist.get('CFBundleName')
        
    # CFBundleIdentifier
    @property
    def bundle_identifier(self):
        return self.plist.get('CFBundleIdentifier')
    
    # CFBundleShortVersionString
    @property
    def bundle_version(self):
        return self.plist.get('CFBundleShortVersionString')
    
    @property
    def plist(self):
        
        if self.__plist:
            return self.__plist
        # 没有缓存的 plist 文件，需要解析并缓存
        ipa = zipfile.ZipFile(self.__ipapath)
    
        for info in ipa.infolist():
            # 查找 Info.Plist 文件，格式如下：
            # Payload/xxx.app/Info.plist
            if re.match('^Payload/(?:.*)\.app/Info.plist$', info.filename):
                # print info.filename
                # 解压文件到临时路径
                tmppath = os.path.join(tempfile.gettempdir(), os.urandom(5))
                ipa.extract(info, tmppath)
                # print tmppath
                # 解析 plist 文件
                plistpath = os.path.join(tmppath, info.filename)
                self.__plist = biplist.readPlist(plistpath)            
                # 删除 plist 文件
                shutil.rmtree(tmppath)
            
                break
        
        return self.__plist


if __name__ == '__main__':
    path = 'D:/workspace/testManageer/static/iosFiles/new/rrkd-ios-test-2.6.1-1-201603031528.ipa'
    # path = '/tmp/not_exists.ipa'
    
    ipa = IPA(path)
    print ipa.bundle_display_name
    print ipa.bundle_name
    print ipa.bundle_identifier
    print ipa.bundle_version
    
    # print ipa.plist
 
 
 
# if __name__ == '__main__':
#     args = sys.argv[1:]
#     if len(args) < 1:
#         print ('Usage: python ipaInfo2.py /path/to/ipa')
#         exit(0);
#   
#     ipa_path = args[0]
#     analyze_ipa_with_plistlib(ipa_path)