from django.contrib import admin
from .models import (
    Country, NewsLetter, Application, Technology,
    Rank, Team, Faq
)

# ----------------------------
# Country Admin
# ----------------------------

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'language', 'currency', 'phone_code', 'is_services_available', 'is_active', 'created_at')
    search_fields = ('name', 'short_name', 'phone_code')
    list_filter = ('is_services_available', 'is_active')


# ----------------------------
# NewsLetter Admin
# ----------------------------

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at')
    search_fields = ('email',)
    list_filter = ('is_active', 'created_at')


# ----------------------------
# Application Admin
# ----------------------------

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'contact_email1', 'version', 'is_active', 'created_at')
    search_fields = ('name', 'contact_email1')
    readonly_fields = ('created_at',)
    list_filter = ('is_active',)


# ----------------------------
# Technology Admin
# ----------------------------

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')


# ----------------------------
# Rank Admin
# ----------------------------

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active', 'created_at')


# ----------------------------
# Team Admin
# ----------------------------

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'position_number', 'is_active')
    search_fields = ('name', 'rank__name')
    list_filter = ('rank', 'is_active')


# ----------------------------
# FAQ Admin
# ----------------------------

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active')
    search_fields = ('question', 'answer')
    list_filter = ('is_active',)
