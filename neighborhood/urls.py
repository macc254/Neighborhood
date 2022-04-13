
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path,include
from django.conf import settings
from django.contrib.auth import views 
from . import views
from django_registration.backends.one_step.views import RegistrationView



urlpatterns=[
    re_path('^$',views.home,name = 'home'),]
