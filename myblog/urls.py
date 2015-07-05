from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'myblog.views.home', name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),

    #user auth urls
    url(r'^login/$', 'myblog.views.login', name = 'login'),
    url(r'^auth/$', 'myblog.views.auth_view', name = 'auth'),
    url(r'^loggedin/$', 'myblog.views.loggedin', name = 'loggedin'),
    url(r'^signup/$', 'myblog.views.signup', name = 'signup'),
    url(r'^logout/$', 'myblog.views.logout'),
    url(r'^invalid/$', 'myblog.views.invalid'),
    url(r'^register/$', 'myblog.views.register', name  = 'register'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
