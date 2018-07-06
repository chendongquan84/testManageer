#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年5月24日

@author: chendq
'''
import random
import getDistance
from map import mapTools

def randomLocation(lat,lon,r):
    newR = getDistance.getDeviator(r)
    newLat = random.uniform(lat - newR,lat + newR )
    newLon = random.uniform(lon - newR,lon + newR )
   
    return {'lon':newLon,'lat':newLat}

def makeCoorDinate(city,address,r_):
    '''生成一个地址附近R千米内的坐标'''
    r = float(r_)
    print 'city:',city,'address:',address
    A = mapTools.getGeocoder(address, city)
    
    print 'A...', A
    
    lonA = A['lng']
    latA = A['lat'] 
    count = 0
    while True:
        count += 1
        B = randomLocation(latA,lonA,r)
        lonB = B['lon']
        latB = B['lat']
        if getDistance.haversine(lonA, latA, lonB, latB) < r*1000:
            return B
        
        
        
        
        
if __name__ == '__main__':
    print makeCoorDinate('成都市','少城大厦',0.001)