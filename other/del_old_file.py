#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年8月25日

@author: chendq
'''

import os

from other import UniversalFunction
from other import fileManger

def sort_dict_list(dict):
    '''对字典建值全为列表的字典建值按倒叙排序'''
    for key in dict :
        dict[key].sort()
        dict[key].reverse()
    return dict


def group_str(strList,regular):
    '''
    将给列表按正则分类并将各值按倒叙排列
    strList:列表数据
    regular：正则表达是
    grouplist：以正则查找出的值为key的分组数据
    '''
    grouplist= {}
    for str in strList:
        key = UniversalFunction.regularFind(regular,str)
        if key not in grouplist:
            grouplist[key] = []
        grouplist[key].append(str)
        
    sort_dict_list(grouplist)    
    return grouplist   

def del_file(path):
    '''删除文件
    path：文件路径'''
    try:
        os.remove(path)
    except Exception, e:
        print e
        
def get_del_files_list(list,count):
    '''获取列表中需删除元素'''
    if len(list) > count:
        return list[count:]
    else:
        return []
    
def del_files_list(path,list):
    for file in list:
        file_dir = '/'.join([path,file])
        print 'delete ',file_dir
        del_file(file_dir)
    return 
        
def del_old_file(dir,reserveFileCount):
    file_list = fileManger.getFileList(dir)
    file_group = group_str(file_list,'(.*)-d*.')
    for group in file_group:
        del_list = get_del_files_list(file_group[group], reserveFileCount)
        del_files_list(dir, del_list)
        
    return 

def get_folder_lost(dir):
    name_list = fileManger.getFileList(dir)
    folder_list = []
    for name in name_list:
        if os.path.isdir('/'.join([dir,name])):
            folder_list.append(name)
    return folder_list
    
if __name__ == '__main__':
    print get_folder_lost('../')
    

        
    
