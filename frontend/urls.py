# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
	'frontend.views',
	url(r'^$', 'inicio', name='vista_inicio'),
	url(r'^posts/ver/(?P<slug>.*)/$', 'posts', name="vista_post"),
)