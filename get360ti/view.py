# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from model360ti.models import Ip
# Create your views here.

def commitPerson(request):
    s = '''
    <form action="/updateips/" method="get">
    Put ips here:<br>
    <textarea rows="30" cols="50" name="ips"></textarea>
    
    <br>
    <input type="submit" value="submit">
    </form>
    '''
    return HttpResponse(s)


def updateips(request):
    obj = request.GET['ips']
    obj = str(obj)
    obj = obj.split(" ")
    for i in obj:
        print i
        i = Ip(name=i)
        i.save()
    return HttpResponse("ip is updated!")
    
    
def getAllIps(request):
    s = "the first line"
    ips = Ip.objects.all()
    for i in ips:
        print i
        s = s + i.name + ":"
    return HttpResponse(s)