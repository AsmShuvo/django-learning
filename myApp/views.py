from django.shortcuts import render
from django.http import HttpResponse 

def testView(req):
    return HttpResponse("testing...")