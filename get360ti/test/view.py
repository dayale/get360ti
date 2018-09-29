'''
Created on 

@author: wangjy
'''

from django.http import HttpResponse


def index(request):
    return HttpResponse("hello! This is a test!")