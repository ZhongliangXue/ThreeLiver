# coding:utf-8
from django.shortcuts import render

from django.http import HttpResponse
from . import models

def index(request):
    return HttpResponse(u"3LiverPET图片分割结果展示")

def patient_name(request):
    patients = models.patient.objects.all()
    return render(request,'PatientIndex.html',{'patients':patients})

def Segmentation_page(request,patientID):
    patient = models.patient.objects.get(pk=patientID)
    return render(request,'Segmentation.html',{'patient':patient})

