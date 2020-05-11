from django.conf.urls import url, include
from django.conf.urls import url, include
from . import views

from django.conf.urls import include, url
from django.contrib import admin
# from main.views import MasterList, ReceptionView



urlpatterns = [
    url(r'^$', views.mainPage),
    url(r'^about_us/$', views.aboutPage),
    url(r'^blog/$', views.blogPage),
    url(r'^prices/$', views.pricesPage),
    url(r'^contacts/$', views.contactsPage),
    url(r'^reserv/$', views.MasterList.as_view(), name='reserv'),
    url(r'^master/(?P<master_id>\d+)/$',views.ReceptionView.as_view(), name='reception'),
    url(r'^date_from_ajax/$', views.date_from_ajax, name='date_from_ajax'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^auth/$', views.MainUserView.as_view()),
    url(r'^personal-page/$', views.person, name='personal'),

]