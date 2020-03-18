#from django.conf.urls import url
#from protwo_ap import views

#urlpatterns = [
#    url('',views.index,name='index'),
#]


# ------------So the inculde function is used to link urls---------------------------
from django.conf.urls import url
from protwo_ap import views

urlpatterns = [
    url('',views.help,name = 'help'),
    url('',views.index,name='index'),
]
