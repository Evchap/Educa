from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model): # page 3
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(models.Model): # page 3
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Module(models.Model): # page 3
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Content(models.Model): # page 6
    module = models.ForeignKey(Module,  related_name='contents', on_delete=models.CASCADE,)
    # content_type = models.ForeignKey(ContentType, on_delete='CASCADE')
    content_type = models.ForeignKey(ContentType, # page 11
                                     limit_choices_to={'model__in': ('text',
                                                                     'video',
                                                                     'image',
                                                                     'file',)},
                                     on_delete=models.CASCADE,
                                     )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class ItemBase(models.Model): # page 11
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase): # page 11
    content = models.TextField()


class File(ItemBase): # page 11
    file = models.FileField(upload_to='files')


class Image(ItemBase): # page 11
    file = models.FileField(upload_to='images')


class Video(ItemBase): # page 11
    url = models.URLField()
