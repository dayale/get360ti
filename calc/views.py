# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.http import HttpRequest
# Create your views here.

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    
    return HttpResponse(str(c))

