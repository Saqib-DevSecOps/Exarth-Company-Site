from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=255, help_text='Enter the name of the category')
    thumbnail_image = models.ImageField(upload_to='blog/categories/thumbnails/', null=True, blank=True)
    description = models.TextField(help_text='Enter a description for the category')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    title = models.CharField(max_length=255)
    thumbnail_image = models.ImageField(upload_to='blog/thumbnails/', null=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE,
                                 help_text='Select a category for the blog')
    content = CKEditor5Field('Content')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog/images/', help_text='Upload an image for the blog')
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog Image'
        verbose_name_plural = 'Blog Images'
        ordering = ['created_at']

    def __str__(self):
        return self.blog.title


class CaseStudyCategory(models.Model):
    name = models.CharField(max_length=255, help_text='Enter the name of the category')
    thumbnail_image = models.ImageField(upload_to='case-study/categories/thumbnails/', null=True, blank=True)
    description = models.TextField(help_text='Enter a description for the category')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Case Study Category'
        verbose_name_plural = 'Case Study Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class CaseStudy(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    title = models.CharField(max_length=255)
    thumbnail_image = models.ImageField(upload_to='case-study/thumbnails/', null=True, blank=True)
    category = models.ForeignKey(CaseStudyCategory, on_delete=models.CASCADE,
                                 help_text='Select a category for the case study')
    industry = models.CharField(max_length=255, help_text='Enter the industry of the case study')

    problem_statement = CKEditor5Field('Problem Statement')
    solution = CKEditor5Field('Solution')
    result = CKEditor5Field('Result')
    summary = CKEditor5Field('Summary')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Case Study'
        verbose_name_plural = 'Case Studies'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class CaseStudyImage(models.Model):
    case_study = models.ForeignKey(CaseStudy, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='case-study/images/', help_text='Upload an image for the case study')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Case Study Image'
        verbose_name_plural = 'Case Study Images'
        ordering = ['created_at']

    def __str__(self):
        return self.case_study.title
