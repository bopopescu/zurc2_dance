#encoding: utf-8

from django.db import models

class Album(models.Model):

	title =  models.CharField(verbose_name=u'Título do Album',
							  max_length=100)
	created_on = models.DateTimeField(auto_now_add=True,
									  verbose_name=u'Criado em')

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Álbum'
		verbose_name_plural = u'Álbuns'

class Photo(models.Model):

	album = models.ForeignKey(Album, verbose_name=u'Album',
							  related_name='albuns')
	title = models.CharField(verbose_name=u'Título',
							 max_length=200,
							 blank=True)
	image = models.ImageField(upload_to=u'photos',
							  verbose_name=u'Imagem')
	primary = models.BooleanField(default=False,
								   verbose_name=u'Principal ?')
	created_on = models.DateTimeField(auto_now_add=True,
									  verbose_name=u'Criado em')
	updated_on = models.DateTimeField(auto_now=True,
									  verbose_name=u'Atualizado em')

	def __unicode__(self):
		if self.title:
			return self.title
		return self.image.name.split('/')[-1]

	class Meta:
		verbose_name = u'Foto'
		verbose_name_plural = u'Fotos'

def photo_pre_save(sender, instance, **kwargs):
	if instance.primary:
		others = Photo.objects.filter(album=instance.album)
		if instance.pk:
			others = others.exclude(pk=instance.pk)
		others.update(primary=False)

models.signals.pre_save.connect(photo_pre_save, sender=Photo)
