from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
url(r'^UI/$', 'tale_teller.info_form.views.UI'),
)


    # url(r'^admin/', include(admin.site.urls)),
	# url(r'^home/$', 'tale_teller.views.home'),
	# url(r'^bio/$', 'tale_teller.views.bio'),
	# url(r'^testimonials/$', 'tale_teller.views.testimonials'),
	# url(r'^services/$', 'tale_teller.views.services'),
	# url(r'^resources/$', 'tale_teller.views.resources'),
	# url(r'^login/$', 'tale_teller.views.login'),