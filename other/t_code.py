#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年10月20日

@author: chendq
'''

#-*- encoding: utf-8 -*-
import logging
import sys
import os
import pygame
from pygame.locals import *
from hubarcode.code128 import Code128Encoder
from PIL import Image,ImageDraw,ImageFont

#logging.getLogger("code128").setLevel(logging.DEBUG)
#logging.getLogger("code128").addHandler(logging.StreamHandler(sys.stdout))
#12-80  10-80 10-60 12-60 10-70 12-70 10-70
'''
使用huBarcode,pygame和PIL生成条形码
'''
if __name__ == "__main__":
    #1 生成条形码
    text = "068080835AD000D10701014111".upper()
    encoder = Code128Encoder(text,options={"ttf_font":"C:/Windows/Fonts/SimHei.ttf","ttf_fontsize":12,
  "bottom_border":15,"height":70,"label_border":2})
    encoder.save("test.png",bar_width=1)
   
#2 生成条码描述
    pygame.init()
    content = u"P07D111140 T07D1111407010 20150321113322"
    font = pygame.font.SysFont('SimHei', 10)
    ftext = font.render(content, True, (0, 0, 0))
    pygame.image.save(ftext, "t.png")
   
#3 合成中文文字到条形码，生成新的条码
    img = Image.open("test.png")
    img_w, img_h = img.size
    icon = Image.open("t.png")
    icon_w, icon_h = icon.size
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)  
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)+35
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    img.save(text+".png") 