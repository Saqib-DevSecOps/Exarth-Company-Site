from django.contrib import admin
from .models import (
    BlogCategory,
    Blog,
    BlogImage,
    CaseStudyCategory,
    CaseStudy,
    CaseStudyImage
)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active']


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'is_featured', 'is_active', 'created_at', 'updated_at']
    list_filter = ['status', 'is_active', 'category']
    search_fields = ['title', 'content']
    inlines = [BlogImageInline]


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ['blog', 'image', 'created_at']
    search_fields = ['blog__title']
    list_filter = ['created_at']
    ordering = ['created_at']


@admin.register(CaseStudyCategory)
class CaseStudyCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active']
    search_fields = ['name', 'description']


class CaseStudyImageInline(admin.TabularInline):
    model = CaseStudyImage
    extra = 1


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'industry', 'status', 'is_active', 'created_at', 'updated_at']
    list_filter = ['status', 'is_active', 'category', 'industry']
    inlines = [CaseStudyImageInline]
    list_editable = ['is_active']


@admin.register(CaseStudyImage)
class CaseStudyImageAdmin(admin.ModelAdmin):
    list_display = ['case_study', 'image', 'created_at']
    search_fields = ['case_study__title']
    list_filter = ['created_at']
    ordering = ['created_at']
