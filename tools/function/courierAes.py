#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年7月5日

@author: chendq
'''

import base64

from Crypto.Cipher import AES

'''
人人快递json数据加密解密模块：

data = '{"test1":"str1","test2":"str2"}'
key = 'UITN25LMUQC436IMUITN25LMUQC436IM' 

A = CourierAes(key)
encrypt_data = A.encrypt(data) # 加密用法
decrypt_data = A.decrypt(encrypt_data) # 解密用法

'''

class CourierAes:
    def __init__(self,key):
        self.block_size = AES.block_size
        self.cipher = AES.new(key)
        
    def _pad(self,s):
        '''补齐'''
        return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)
    
    def _unpad(self,s):
        return s[0:-ord(str(s)[-1])]
    
    def encrypt(self,data):
        '''加密'''
        return base64.b64encode(self.cipher.encrypt(self._pad(data)))
    
    def decrypt(self,data):
        '''解密'''
        data = base64.b64decode(data)
        return self._unpad(self.cipher.decrypt(data))



