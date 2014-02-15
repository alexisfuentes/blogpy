# -*- coding: utf-8 -*-
from django.db import models

estado = (
	('b', 'borrado'),
	('p', 'publicado'),
	('e', 'espera')
)
estadoU = (
	('a', 'activo'),
	('i', 'inactivo')
)

class Medio(models.Model):
	images = models.ImageField(upload_to='images')

	def __unicode__(self):
		return u"%s" % (self.images)

class autor(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	fecha = models.DateField(auto_now_add=True)
	usuario = models.CharField(max_length=50)
	contrasena = models.CharField(max_length=50)
	estado = models.CharField(max_length=1, choices=estadoU)

	class Meta:
		verbose_name = u'autor'
		verbose_name_plural = u'autores'

	def __unicode__(self):
		return "%s %s" %(self.nombre, self.apellidos)


class categoria(models.Model):
	"""docstring for categoria"""
	nombre = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	class Meta:
		verbose_name=u'categoria'
		verbose_name_plural=u'categorias'

	def __unicode__(self):
		return self.nombre
    

class entrada(models.Model):
	''' docstring for entrada '''
	titulo = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	autor = models.ForeignKey(autor)
	texto = models.TextField()
	fecha = models.DateTimeField(db_index=True, auto_now_add=True)
	estatus = models.CharField(max_length=1, choices=estado)
	categoria = models.ManyToManyField(categoria)

	class Meta:
		verbose_name=u'entrada'
		verbose_name_plural=u'entradas'

	def __unicode__(self):
		return self.titulo

class comentario(models.Model):
	autor = models.ForeignKey(autor)
	post = models.ForeignKey(entrada)
	comentario = models.CharField(max_length=200)

	class Meta:
		verbose_name = u'comentario'
		verbose_name_plural = u'comentarios'

	def __unicode__(self):
		return self.comentario