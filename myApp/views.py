from django.shortcuts import render
from django.http import HttpResponse 
import datetime
def testView(req):
    return HttpResponse("testing...")

def timeView(req):
    date = datetime.datetime.now()
    res = "Time is {}".format(date)
    return HttpResponse(res)
    