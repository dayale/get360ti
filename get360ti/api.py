# -*- coding: utf-8 -*-

'''
Created on 

@author: wangjy
'''
from __future__ import unicode_literals

from django.http import HttpResponse
from django.core import exceptions

from model360ti.models import Ip
# Create your views here.



def getAllIps(request):
    ips = Ip.objects.all()
    s = ""
    for i in ips:
        print i
        s = s + i.name + ":"
        print s.toJson()
    print s
    return HttpResponse(s)


def updateIpInfo(request):
    
    try:
        ip = Ip.objects.get(name=request.GET['ip'])
        ip.delete()
    except :
        pass
    
    return HttpResponse(request.GET['ip'])
    