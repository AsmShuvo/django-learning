from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse  
import datetime
from .models import GeeksModel
from .forms import GeeksForm


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



def create_view(req):
    context = {}
    form = GeeksForm(req.POST or None)
    if(form.is_valid()):
        form.save()
    
    context['form'] = form
    return render(req, "create_view.html", context)



def detail_view(req, id):
    context ={}
    context["data"] = GeeksModel.objects.get(id=id)
    return render(req, "detail_view.html", context)



def update_view(req, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    form = GeeksForm(req.POST or None, instance=obj)
    
    if(form.is_valid()):
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form
    return render(req, 'update_view.html', context)



def delete_view(request, id): 
    context ={}
    obj = get_object_or_404(GeeksModel, id = id)

    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)



    
    
    
    
    
    