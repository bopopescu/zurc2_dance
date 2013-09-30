#encoding: utf-8

from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import signals
from django.template.defaultfilters import slugify

from signals import create_slug

class Rhythm(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=150,
        help_text=u'O nome do rítimo')
    user = models.ForeignKey(User, verbose_name=u'Usuário',
                             null=True, blank=True)
    slug = models.SlugField(verbose_name=u'Apelido', max_length=100,
                            help_text=u'Preenchimento automático', unique=True,
                            blank=True, null=True, editable=False)

    description = models.TextField(verbose_name=u'Descrição',
        blank=True)

    photo = models.ImageField(upload_to='rhythms', verbose_name=u'Foto',
        null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True,
        verbose_name=u'Criado em')
    update_on = models.DateTimeField(auto_now=True,
        verbose_name=u'Atualizado em')
    public = models.BooleanField(verbose_name=u'Público ?',
                                 default=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name).replace('_','')
            while Rhythm.objects.filter(slug = self.slug):
                self.slug += '-1'
        super(Rhythm, self).save()

    def dancestep_count(self):
        return self.dancesteps.count()
    dancestep_count.short_description = u'Número de Passos'


    @models.permalink
    def get_absolute_url(self):
        return ('rhythms_details', (), {'pk': self.pk})


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Rítmo'
        verbose_name_plural = u'Rítmos'
        ordering =['name']

signals.post_save.connect(create_slug, sender=Rhythm)

class Level(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=150,
        help_text=u'O nome do nível')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Nível'
        verbose_name_plural = u'Níveis'
        ordering = ['name']

class DanceStep(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=200,
                            help_text=u'O nome do passo de dança')
    slug = models.SlugField(verbose_name=u'Apelido', 
                            help_text=u'Preenchimento automático', unique=True,
                            blank=True, null=True, editable=False)

    rhythm = models.ForeignKey(Rhythm, verbose_name=u'Ritmo',
                               related_name=u'dancesteps', null=True, blank=True)
    level = models.ForeignKey(Level, verbose_name=u'Nível',
                              related_name=u'level', null=True, blank=True)
    description = models.TextField(verbose_name=u'Descrição',
                                   blank=True)
    link = models.URLField(verbose_name=u'link de video', max_length=200)

    photo = models.ImageField(upload_to='dancesteps', verbose_name=u'Foto',
        null=True, blank=True)

    dica = models.TextField(verbose_name=u'Dicas/macetes', blank=True)
    features = models.BooleanField(verbose_name="Preferidos", default=True, blank=True)


    def save(self):
        if not self.id:
            self.slug = slugify(self.name).replace('_','')
            while DanceStep.objects.filter(slug = self.slug):
                self.slug += '-1'
        super(DanceStep, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('dancesteps',(), {'slug': self.slug})


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Passo'
        verbose_name_plural = u'Passos'
        ordering = ['name']

