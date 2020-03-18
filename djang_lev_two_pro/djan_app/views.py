from django.shortcuts import render
from djan_app.models import User
# Create your views here.

def index(request):
    return render(request,'djan_app/index.html')

def users(request):
    user_list = User.objects.order_by('First_Name')
    user_dict = {'users':user_list}
    return render(request,'djan_app/user.html',context = user_dict)
