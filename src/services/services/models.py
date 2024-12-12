import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class ServiceCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, help_text=_('Enter the name of the service category'))
    slug = models.SlugField(unique=True, help_text=_('URL-friendly identifier for the service category'))
    description = models.TextField(help_text=_('Enter the description of the service category'))
    thumbnail_image = models.ImageField(upload_to='services/categories/',
                                        help_text=_('Upload an image for the service category'))
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                               help_text=_('Select the parent category for this category'))
    is_active = models.BooleanField(default=True, help_text=_('Is the category currently active?'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Service Category')
        verbose_name_plural = _('Service Categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    STATUS_CHOICES = [
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('archived', _('Archived')),
    ]
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255, help_text=_('Enter the title of the service'))
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    short_description = models.TextField(help_text=_('Enter a short description of the service'))
    thumbnail_image = models.ImageField(upload_to='services/thumbnails/',
                                        help_text=_('Upload a thumbnail image for the service'))
    content = CKEditor5Field('Content', config_name='extends')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text=_('Select the status of the service'))
    is_featured = models.BooleanField(default=False, help_text=_('Is this a featured service?'))

    service_technologies = models.ManyToManyField('company.Technology', through='ServiceTechnology')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='services/images/', help_text=_('Upload an image for the service'))
    description = models.TextField(blank=True, help_text=_('Enter a description for the image'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Service Image')
        verbose_name_plural = _('Service Images')

    def __str__(self):
        return f"Image for {self.service.title}"


class ServiceVideo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='services/videos/', help_text=_('Upload a video for the service'))
    description = models.TextField(blank=True, help_text=_('Enter a description for the video'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Service Video')
        verbose_name_plural = _('Service Videos')

    def __str__(self):
        return f"Video for {self.service.title}"


class ServiceTechnology(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='technologies')
    technology = models.ForeignKey('company.Technology', on_delete=models.CASCADE, max_length=255,
                                   help_text=_('Enter the name of the technology'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Service Technology')
        verbose_name_plural = _('Service Technologies')

    def __str__(self):
        return self.service.title
