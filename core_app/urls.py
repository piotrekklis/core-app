from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logged_out/', views.logged_out, name='logged_out'),
    url(r'^add_core_object/edit_core_object/(?P<core_object_id>[0-9]+)/', views.edit_core_object, name= 'edit_core_object'),
    url(r'^add_core_object/', views.add_core_object, name='add_core_object'),
]