
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path,include
from django.conf import settings
from django.contrib.auth import views 
from . import views
from django_registration.backends.one_step.views import RegistrationView



urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    re_path('accounts/', include('django_registration.backends.one_step.urls')),
    re_path('accounts/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    ]
