from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$', 'clients.views.client_news'),
 	url(r'^news/$', 'clients.views.client_news'),
	url(r'^profile/$', 'clients.views.client_profile'),
	url(r'^projects/$', 'clients.views.client_projects'),
	url(r'^message/$', 'clients.views.client_message'),
	url(r'^authorpage/$', 'clients.views.client_authorpage'),
    url(r'^projpost/$', 'clients.views.projpost'),
    url(r'^projpost/newproj/$', 'clients.views.newproj'),
    url(r'^draftpost/(\d+)/$', 'clients.views.draftpost'),
    url(r'^draftpost/(\d+)/newdraft/$', 'clients.views.newdraft'),
    url(r'^commpost/(\d+)/$', 'clients.views.commpost'),
    url(r'^commpost/(\d+)/newcomm/$', 'clients.views.newcomm'),

    url(r'^profilepost/$', 'clients.views.profilepost'),
    url(r'^profilepost/newprofile/$', 'clients.views.newprofile'),

	url(r'^forums/$', 'clients.views.forums'),
	url(r'^forums/topic/(\d+)/$', 'clients.views.topics'),
	url(r'^forums/thread/(\d+)/$', 'clients.views.threads'),
	url(r'^forums/post/(new_thread|reply)/(\d+)/$', 'clients.views.posts'),
	url(r'^forums/reply/(\d+)/$', 'clients.views.reply'),
	url(r'^forums/new_thread/(\d+)/$', 'clients.views.new_thread'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

