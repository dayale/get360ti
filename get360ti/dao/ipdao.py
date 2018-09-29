'''
Created on 

@author: wangjy
'''
from model360ti.models import Ip


class IpDao(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
      
    def InsertIP(self,ipstr):
        self._ip = Ip(name=ipstr)
        self._ip.save()
        return "OK"
    
    def GetIP(self,ipstr):
        return Ip.objects.filter(name=ipstr)
    def GetAllIP(self):
        l = Ip.objects.all()
        return l

    