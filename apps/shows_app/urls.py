from django.conf.urls import url
from . import views	
                    
urlpatterns = [
    # url(r'^$', views.index),
    url(r'^shows/new$',views.shownew),
    url(r'^shows/create$',views.showcreate),
    url(r'^shows/(?P<id>\d+)$',views.showeach),
    url(r'^shows$',views.showall),
    url(r'^shows/(?P<id>\d+)/edit$',views.showedit),
    url(r'^shows/edit$',views.editdetail),
    url(r'^shows/(?P<id>\d+)/delete$',views.showdelete),
]