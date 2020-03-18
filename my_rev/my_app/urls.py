from django.conf.urls import url 
from my_app import views

urlpatterns = [
    url('',views.index,name = 'index'),
]
