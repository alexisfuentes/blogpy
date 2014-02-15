from django.conf.urls import patterns, url

urlpatterns = patterns(
	'backend.views',
	url(r'^$', 'inicio', name='vista_inicio_admin'),
	url(r'^post/nuevo/$', 'agregar_post', name='vista_agregar_post'),
	url(r'^post/editar/(\d+)/$', 'editar_post', name='vista_editar_admin'),
	url(r'^post/borrar/(\d+)/$', 'borrar_post', name='vista_borrar_admin'),
)