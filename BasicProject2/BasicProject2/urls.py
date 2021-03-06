"""
Definition of urls for BasicProject2.
"""

from django.conf.urls import include, url
from HelloDjangoApp.views import index, about

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^home$', index, name = 'home'),
    url(r'^about$', about, name ='about'),
    # Examples:
    # url(r'^$', BasicProject2.views.home, name='home'),
    # url(r'^BasicProject2/', include('BasicProject2.BasicProject2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
