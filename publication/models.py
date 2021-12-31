from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField

class Topic(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')

    class Meta:
        ordering = ('name',)
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

    def __str__(self):
        return self.name

    
