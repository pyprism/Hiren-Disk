from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hiren.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'disk.views.index'),
    url(r"^login$", 'disk.views.login'),
    url(r"^logout$", 'disk.views.logout'),
    url(r"^browse$", 'disk.views.browse'),
    url(r"^search$", 'disk.views.search'),
    url(r"^add$", 'disk.views.add'),
    url(r"^json$", 'disk.views.json'),
    url(r"^browse/(?P<disk>\d+)/$", 'disk.views.disk_names'),
)
