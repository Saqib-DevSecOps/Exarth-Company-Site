from django.contrib import admin
from .models import (
    Country, NewsLetter, Application, Technology,
    Rank, Team, Faq, TeamMemberQualification, TeamMemberExperience, TeamMemberSkill, TeamMemberCertificate
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



# Inline admin for TeamMemberQualification
class TeamMemberQualificationInline(admin.TabularInline):
    model = TeamMemberQualification
    extra = 1  # Number of empty forms to display
    fields = ['title', 'institution', 'year_completed']
    max_num = 10  # Limit to 10 qualifications

# Inline admin for TeamMemberExperience
class TeamMemberExperienceInline(admin.TabularInline):
    model = TeamMemberExperience
    extra = 1
    fields = ['position', 'company', 'start_date', 'end_date', 'description']
    max_num = 10

# Inline admin for TeamMemberSkill
class TeamMemberSkillInline(admin.TabularInline):
    model = TeamMemberSkill
    extra = 1
    fields = ['technology', 'proficiency_level']
    max_num = 10

# Inline admin for TeamMemberCertificate
class TeamMemberCertificateInline(admin.TabularInline):
    model = TeamMemberCertificate
    extra = 1
    fields = ['title', 'issuing_organization', 'issue_date', 'expiration_date', 'certificate_url', 'thumbnail_image']
    max_num = 10

# Main admin for Team
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position_number', 'rank', 'is_active']
    search_fields = ['name', 'rank__name']
    list_filter = ['rank', 'is_active']
    inlines = [
        TeamMemberQualificationInline,
        TeamMemberExperienceInline,
        TeamMemberSkillInline,
        TeamMemberCertificateInline,
    ]
    fieldsets = (
        (None, {
            'fields': ('name', 'position_number', 'rank', 'profile_image', 'description', 'is_active')
        }),
        ('Social Links', {
            'fields': ('facebook_link', 'instagram_link', 'linkedin_link', 'twitter_link', 'github_link')
        }),
    )



# ----------------------------
# FAQ Admin
# ----------------------------

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active')
    search_fields = ('question', 'answer')
    list_filter = ('is_active',)
