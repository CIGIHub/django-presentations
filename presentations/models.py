from django.db import models
from django.utils.text import slugify
import re


class UniquelySlugable(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:255]

            while type(self).objects.filter(slug=self.slug).exists():
                match_obj = re.match(r'^(.*)-(\d+)$', self.slug)
                if match_obj:
                    next_int = int(match_obj.group(2)) + 1
                    self.slug = match_obj.group(1) + "-" + str(next_int)
                else:
                    self.slug += '-2'

        super(UniquelySlugable, self).save(*args, **kwargs)


class Presentation(UniquelySlugable):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    author = models.CharField(max_length=1024)
    slides = models.ManyToManyField('Slide', through='OrderedSlides',
                                    null=True, blank=True)

    def __unicode__(self):
        return self.title


class OrderedSlides(models.Model):
    presentation = models.ForeignKey('Presentation')
    slide = models.ForeignKey('Slide')
    order = models.IntegerField()

    class Meta:
        ordering = ('order', )

    def __unicode__(self):
        return "%s - %d: %s" % (self.presentation.title, self.order, self.slide.title)


class Slide(UniquelySlugable):
    title = models.CharField(max_length=1024)
    body = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title
