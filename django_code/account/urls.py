from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'), #Used for the UI for both creation and logging in
    url(r'^createAccount$', views.createAccount, name='createAccount'), #Used by POST for creation
]
