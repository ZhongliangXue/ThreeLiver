#coding:utf-8

from django.db import models

class patient(models.Model):
    name = models.CharField(max_length=30)
    tel = models.CharField(u'电话号码',max_length=15)
    patientID = models.IntegerField()


    def __str__(self):
        return self.name
