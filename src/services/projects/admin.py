from django.contrib import admin
from .models import (
    ProjectCustomer,
    ProjectCategory,
    Project,
    ProjectKeyFeature,
    ProjectChallenge,
    ProjectTechnology,
    ProjectImage,
    ProjectVideo,
    ProjectTestimonial,
)

# Inline Models
class ProjectTechnologyInline(admin.TabularInline):  # You can use StackedInline if you prefer a stacked layout
    model = ProjectTechnology
    extra = 1  # Number of empty forms to display
    verbose_name = 'Technology'
    verbose_name_plural = 'Technologies'


class ProjectKeyFeatureInline(admin.TabularInline):
    model = ProjectKeyFeature
    extra = 1
    verbose_name = 'Key Feature'
    verbose_name_plural = 'Key Features'


class ProjectChallengeInline(admin.TabularInline):
    model = ProjectChallenge
    extra = 1
    verbose_name = 'Challenge'
    verbose_name_plural = 'Challenges'


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    verbose_name = 'Image'
    verbose_name_plural = 'Images'


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1
    verbose_name = 'Video'
    verbose_name_plural = 'Videos'


class ProjectTestimonialInline(admin.TabularInline):
    model = ProjectTestimonial
    extra = 1
    verbose_name = 'Testimonial'
    verbose_name_plural = 'Testimonials'


# Project Admin Class
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'customer', 'category', 'start_date', 'end_date', 'budget', 'status', 'project_tier']
    search_fields = ['title', 'customer__name', 'category__name']
    list_filter = ['status', 'project_tier']
    inlines = [
        ProjectTechnologyInline,
        ProjectKeyFeatureInline,
        ProjectChallengeInline,
        ProjectImageInline,
        ProjectVideoInline,
        ProjectTestimonialInline,
    ]


# Register your models
admin.site.register(ProjectCustomer)
admin.site.register(ProjectCategory)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectKeyFeature)
admin.site.register(ProjectChallenge)
admin.site.register(ProjectImage)
admin.site.register(ProjectVideo)
admin.site.register(ProjectTestimonial)
