
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path,include
from django.conf import settings
from django.contrib.auth import views 
from . import views
from . import views as app_views
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView



urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    re_path('accounts/', include('django_registration.backends.one_step.urls')),
    re_path('accounts/register/',
        RegistrationView.as_view(success_url='/home/'),
        name='django_registration_register'),
    re_path(r'^new/post$', views.new_post, name='new-post'),
    re_path('accounts/', include('django_registration.backends.one_step.urls')),
    re_path(r'^new/post$', views.new_post, name='new-post'),
    re_path(r'^update/',app_views.update_profile,name='update_profile'),
    re_path('accounts/profile/',views.profile,name='profile'),
    re_path(r'^feeds_profile/(?P<pk>\d+)$',app_views.users_profile,name='users_profile'), 
    re_path('new-hood/', views.create_hood, name='new-hood'),


    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)