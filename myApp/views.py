from django.shortcuts import render
from django.http import HttpResponse 
import datetime
from .models import GeeksModel
def testView(req):
    return HttpResponse("testing...")

def timeView(req):
    date = datetime.datetime.now()
    res = "Time is {}".format(date)
    return HttpResponse(res)

def list_view (req):
    context = {}
    context["dataset"] = GeeksModel.objects.all()
    return render(req, "list_view.html", context)
    