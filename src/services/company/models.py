import uuid

from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='companies/logos/')
    website = models.URLField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

    def __str__(self):
        return self.name


class Technology(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255, help_text='Enter the name of the technology')
    description = models.TextField(help_text='Enter a description for the technology')
    thumbnail_image = models.ImageField(upload_to='technologies/thumbnails/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                               help_text='Select a parent technology')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ['title']

    def __str__(self):
        return self.title


