from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey(Collection, null=True, blank=True)
    themes = models.ManyToManyField('Theme')


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book)
    main_theme = models.ForeignKey(Theme)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
