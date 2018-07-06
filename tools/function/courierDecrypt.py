#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年7月7日

@author: chendq
'''

import base64
import time
import json

from courierAes import CourierAes

def _get_requests_data(requestsData):
    '''将请求出去base64解码'''
    return base64.b64decode(requestsData)

def _get_json_str(data):
    '''获取请求数据中json数据包'''
    lit = data.split('@_@')
    return lit[1]

def decrypt(str):
    '''Aes数据解码'''
    s = CourierAes('FCD4972BE9D7D46BEAB6C47708C1B676')
    return s.decrypt(_get_json_str(_get_requests_data(str)))

if __name__ == '__main__':
    data = 'OTI2NzU2MWRlYjRiYjljOTMwZGRjMDNhMjlkMmRkZTBAX0BYTWtnMzdySzZPYndlM3I4dEJlUjArWXhDNGEvU0NoYTV0ZDZ0cWplQUR1U25hVHJHNFo1Z2IySHFNSllFODR1K0dPN2gyNkk1MHk3aGhnSERMSk1FV1NDb3hPeldUbG4zNUZzVHRwS2MvdXoydkowbFMvVXVCZ0tvYVFlTGRJem53dmgrSzBvSldOQkhZL2x4SW5xaElDZm1XSHczY1RzbitkQW80a3ZEeWZoV2s2K3FJbGVMZ2FNQ3M0UTk1dnp4OUVzTlB3TGY4eGxxN0JCM2JJaFlwMEZQa1h2Y2xwazd5SVJWaWgxLytObGwzeEtzUXQvcFFBZFdTRlRrWHE4MFFaVFhLU0VGQUg0MkQxKzF0bUlsL0hWTmowS1ZBaGsyL242ekpSUmVaSEd2WFp6emJNdFlnakUrbWdzS1VrUjlROU5iNTUxUHNLKzZ5TEdsSHZxSWhFODBKbUtWcUxndFl0V3RzU3JBSDlKTi84NlJpZXA2Y0hqTFp4T1dZV1hFdGNQcjFXYnBNSTdveVZCa1JxNEpjU0V2azFYM2poRS9sWENseStWNGZmTHNmVGVSRnl4QUJVNlpIaG4vMW5pSVFLVWZJZUJ3MXIxWEVaNkZKeWdCdz09'
    print decrypt(data)
    