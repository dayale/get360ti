'''
Created on 

@author: wangjy
'''

class IPs(object):
    '''
    classdocs
    '''


    def __init__(self, ipstr):
        '''
        Constructor
        '''
        self._ip = ipstr
        
    def setIP(self,ipstr):
        self._ip = ipstr
        
    def getIP(self):
        return self._ip