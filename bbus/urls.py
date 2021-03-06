from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbus.views.home', name='home'),
    # url(r'^bbus/', include('bbus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bbus.views.index', name='index'),
    url(r'^search$', 'bbus.views.search', name='search'),
    url(r'^api/v1/search/', 'bbus.views.api', name='search'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
