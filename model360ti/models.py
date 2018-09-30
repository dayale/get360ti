# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import models

# Create your models here.
class Ip(models.Model):
    name = models.CharField(max_length=20)
    

    
class IpInfo(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=2000)
    loc = models.CharField(max_length=100)
    
