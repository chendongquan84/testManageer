#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月24日

@author: chendq
'''

from math import radians, cos, sin, asin, sqrt,degrees
from decimal import *
import random 

# import math
      
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    print haversine(104.12078502178,30.686386648837,104.06429619728,30.66534559038)
    >>> 5887.19050049
    """  
    # 将十进制度数转化为弧度  
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
    # haversine公式  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 # 地球平均半径，单位为公里  
    
    return c * r *1000

def getDeviator(r):
    '''获得坐标最大偏差量'''
    earth_r = 6371 # 地球平均半径，单位为公里
    print Decimal(float(r))/earth_r
    return degrees(Decimal(r)/Decimal(earth_r))

# {u'lat': 30.686386648837, u'lng': 104.12078502178}
# {u'lat': 30.66534559038, u'lng': 104.06429619728}
if __name__ == '__main__':
    x = 30.686386648837 + getDeviator(5)
    print haversine(104.12078502178,30.686386648837 ,104.12078502178 + getDeviator(5),30.686386648837)
    
    
    
    
    
