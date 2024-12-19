from django.contrib import admin
from .models import ServiceCategory, Service, ServiceImage, ServiceVideo, ServiceTechnology


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ['name']


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1
    fields = ('image', 'description')
    readonly_fields = ('created_at', 'updated_at')


class ServiceVideoInline(admin.TabularInline):
    model = ServiceVideo
    extra = 1
    fields = ('video', 'description')
    readonly_fields = ('created_at', 'updated_at')


class ServiceTechnologyInline(admin.TabularInline):
    model = ServiceTechnology
    extra = 1
    fields = ('technology',)
    readonly_fields = ('created_at', 'updated_at')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('status', 'category', 'is_featured')
    search_fields = ('title', 'category__name')
    ordering = ['-created_at']
    inlines = [ServiceImageInline, ServiceVideoInline, ServiceTechnologyInline]


class ServiceTechnologyAdmin(admin.ModelAdmin):
    list_display = ('service', 'technology', 'created_at', 'updated_at')
    search_fields = ('service__title', 'technology__title')
    ordering = ['service', 'technology']


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage)
admin.site.register(ServiceVideo)
admin.site.register(ServiceTechnology, ServiceTechnologyAdmin)
