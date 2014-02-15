# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from frontend.models import entrada, comentario

def inicio(request):
	post = entrada.objects.all()
	con = {'post' : post}
	return render_to_response("frontend/inicio.html", con)

def posts(request, slug):
	contenido = entrada.objects.get(slug = slug)
	coment = comentario.objects.filter(post = contenido)
	c = {'contenido' : contenido, 'comentarios' : coment}
	return render_to_response("frontend/vista_post.html", c)
