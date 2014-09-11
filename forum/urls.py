from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	(r'^$', 'forum.views.main'),
	(r'^forum/(\d+)/$', 'forum.views.forum'),
	(r'^thread/(\d+)/$', 'forum.views.thread'),
	
	(r'^post/(new_thread|reply)/(\d+)/$', 'forum.views.post'),
	(r'^reply/(\d+)/$', 'forum.views.reply'),
	(r'^new_thread/(\d+)/$', 'forum.views.new_thread'),
)