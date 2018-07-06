#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年6月1日

@author: chendq
'''
import requests
import json
def getGeocoder(address,city):
    '''
    调用方法： getGeocoder('少城大厦','成都市')
   返回结果： {u'lat': 30.66534559038, u'lng': 104.06429619728}
    '''
    url = 'http://api.map.baidu.com/geocoder/v2/'
    params_ = {'address':'%s' % address,
               'output':'json',
               'ak':'P9PycMcSMM2epVUzCMIOlGFY',
               #'ad':'4032f6db1085b0c63683ef3917e40428',
               'city':city}
    
    res = requests.get(url, params_)
    try:
        geocoder = res.json()['result']['location']
        return geocoder
    except:
        print 'getGeocoder：获取地理位置失败'
        return None
def Geocoder(lat,lng):
    # http://api.map.baidu.com/geocoder/v2/?ak=E4805d16520de693a3fe707cdc962045&callback=renderReverse&location=39.983424,116.322987&output=json&pois=1
    # callback=renderReverse&location=39.983424,116.322987&output=json&pois=1
    url = 'http://api.map.baidu.com/geocoder/v2/'
    #url = 'http://api.map.baidu.com/geocoder/v2/?ak=P9PycMcSMM2epVUzCMIOlGFY&callback=renderReverse&location=%s,%s&output=json&pois=1' % (lat,lng)
    #url = 'http://api.map.baidu.com/geocoder/v2/?ak=P9PycMcSMM2epVUzCMIOlGFY&location=39.983424,116.322987&output=json&pois=0'
    location = '%s,%s' % (lat,lng)
    params_ = {#'callback':'renderReverse',
               'location':location,
               'output':'json',
               'ak':'P9PycMcSMM2epVUzCMIOlGFY',
               'pois':'0'}
    res = requests.get(url,params_)
    print res.json()
    print res.json()['result']['addressComponent']['province'].encode('utf-8') #.encode('utf-8')
    
def distancedeWalking(origin,destination,origin_region,destination_region):
    
    url = 'http://api.map.baidu.com/direction/v1'
    
    payload = {"mode":"walking",
                "origin":"%s" % origin,
                "destination":'%s' % destination,
                "origin_region":"%s" % origin_region,
                "destination_region":"%s" % destination_region,
                "output":"json",
                "ak":"P9PycMcSMM2epVUzCMIOlGFY",
                #'ak':'4032f6db1085b0c63683ef3917e40428',
                "tactics":"12",
               }
    
    res = requests.get(url,params=payload)
    
    if res.json()['type'] == 2:
        return res.json()['result']['routes'][0]['distance']
    else:
        return '输入地址不准确'
    
    
if __name__ == '__main__':
    print getGeocoder('少城大厦','成都市')