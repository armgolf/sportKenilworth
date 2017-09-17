from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.club_list, name='club_list'),
    url(r'^events/$', views.event_list, name='event_list'),
    url(r'^contact/$', views.contact, name='contact'),
]
