from django.shortcuts import render, render_to_response
# Manejo de redirecciones.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from frontend.models import autor, entrada, comentario, categoria, Medio
# Para poder utilizar la variables MEDIA_URL y STATIC_URL se necesita
# importar de django.template la clase RequestContext.

def inicio(request):
	entradas = entrada.objects.all()
	images = Medio.objects.all()
	c = {'post' : entradas, 'images' : images}
	return render_to_response(	"backend/inicio.html", 
								c, 
								context_instance=RequestContext(request)
								)

def agregar_post(request):
	return render_to_response( "backend/nuevo_post.html", 
								context_instance=RequestContext(request))

def editar_post(request, id_post):
	datos = entrada.objects.get(pk=id_post)
	# autor = autor.objects.get(pk=1)
	c = {'post' : datos}
	return render_to_response(	"backend/editar_post.html", 
								c, 
								context_instance=RequestContext(request))

def borrar_post(request, id_post):
	return HttpResponseRedirect('/blog-admin/')