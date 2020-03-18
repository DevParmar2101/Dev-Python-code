from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#def index(request):
#    return HttpResponse("<h1><b><em>The is Is The Second Project</em></b></h1>")

def index(request):
    my_dict = {"insert_me":"hello i am from views.py !"}
    return render(request,"protwo_ap/index.html",context=my_dict)


def help(request):
    helpdict = {"help_insert":"Hello i Am From protwo/help.html ! Somebody Please Help Me !"}
    return render(request,'protwo_ap/help.html',context = helpdict)
