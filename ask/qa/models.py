from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Question(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    added_ad = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='for_likes')

    def __unicode__(self):
        return u'%s, %s' % (self.title, self.author)

    def get_absolute_url(self):
        return reverse('qa.views.question', args=[str(self.id)])


class Answer(models.Model):
    text = models.TextField()
    added_ad = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
