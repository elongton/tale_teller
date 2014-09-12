from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^clients/', include('clients.urls')),
	(r'^forum/', include('forum.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/$', 'tale_teller.views.home'),
    url(r'^$', 'tale_teller.views.home'),
	url(r'^bio/$', 'tale_teller.views.bio'),
	url(r'^testimonials/$', 'tale_teller.views.testimonials'),
	url(r'^services/$', 'tale_teller.views.services'),
	url(r'^resources/$', 'tale_teller.views.resources'),
	url(r'^kaylynnespauls/$', 'tale_teller.views.kaylynnespauls'),
	
	
	url(r'^accounts/login/$', 'tale_teller.views.login'),
	url(r'^accounts/auth/$', 'tale_teller.views.auth_view'),
	url(r'^accounts/loggedin/$', 'tale_teller.views.loggedin'),
	url(r'^accounts/invalid/$', 'tale_teller.views.invalid_login'),
	url(r'^accounts/logout/$', 'tale_teller.views.logout'),
	
	
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
