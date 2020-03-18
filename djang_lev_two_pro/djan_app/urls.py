from django.conf.urls import url
from djan_app import views

urlpatterns = [
    url('',views.users,name='users'),

]
