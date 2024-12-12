import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django_resized import ResizedImageField
from phonenumber_field.formfields import PhoneNumberField


# ----------------------------
# Country Model
# ----------------------------

class Country(models.Model):
    """
    Represents a country with relevant information.
    """
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=2, unique=True, help_text='ISO 3166-1 alpha-2 code')
    language = models.CharField(max_length=3, default='en', help_text='ISO 639-1 language code', null=True, blank=True)
    currency = models.CharField(max_length=3, default='USD', help_text='ISO 4217 currency code', null=True, blank=True)
    phone_code = models.CharField(max_length=4, default='+1', help_text='Phone code (e.g., +1)', null=True, blank=True)

    is_services_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


# ----------------------------
# NewsLetter Model
# ----------------------------

class NewsLetter(models.Model):
    """
    Represents a newsletter subscription.
    """
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email

    def clean(self):
        if NewsLetter.objects.filter(email=self.email).exists():
            raise ValidationError(f"{self.email} is already subscribed to our newsletter.")


# ----------------------------
# Application Model
# ----------------------------

class Application(models.Model):
    """
    Represents application settings and configurations.
    """
    name = models.CharField(max_length=100, help_text='Application name', default='Exarth')
    short_name = models.CharField(max_length=10, help_text='Short name for the application', default='EX')
    tagline = models.CharField(max_length=100, help_text='Business tagline', default='Your digital partner')
    description = models.TextField(default="Add your project description here.", help_text='Application description')

    favicon = ResizedImageField(
        upload_to='core/application/images', null=True, blank=True,
        size=[250, 250], quality=75, force_format='PNG', help_text='Application favicon'
    )
    logo = ResizedImageField(
        upload_to='core/application/images', null=True, blank=True,
        size=[500, 500], quality=75, force_format='PNG', help_text='Application logo'
    )
    logo_dark = ResizedImageField(
        upload_to='core/application/images', null=True, blank=True,
        size=[500, 500], quality=75, force_format='PNG', help_text='Dark theme logo'
    )
    logo_light = ResizedImageField(
        upload_to='core/application/images', null=True, blank=True,
        size=[500, 500], quality=75, force_format='PNG', help_text='Light theme logo'
    )

    contact_email1 = models.EmailField(max_length=100, default='support@exarth.com', help_text='Primary contact email')
    contact_email2 = models.EmailField(max_length=100, default='support@exarth.com', help_text='Secondary contact email')
    contact_phone1 = PhoneNumberField(help_text='Primary contact phone')
    contact_phone2 = PhoneNumberField(help_text='Secondary contact phone')

    address = models.CharField(max_length=255, default='Main office address', help_text='Office address')
    latitude = models.DecimalField(max_digits=10, decimal_places=6, default=23.7, help_text='Latitude')
    longitude = models.DecimalField(max_digits=10, decimal_places=6, default=90.3, help_text='Longitude')

    terms_url = models.URLField(max_length=255, default='https://exarth.com/terms-of-use/', help_text='Terms of use link')

    facebook = models.URLField(max_length=255, default='https://facebook.com/exarth', help_text='Facebook link')
    instagram = models.URLField(max_length=255, default='https://instagram.com/exarth', help_text='Instagram link')
    twitter = models.URLField(max_length=255, default='https://twitter.com/exarth', help_text='Twitter link')

    version = models.CharField(max_length=10, default='1.0.0', help_text='Current application version')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Applications"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if Application.objects.exists() and not self.pk:
            raise ValidationError("Only one application record is allowed.")
        super().save(*args, **kwargs)


# ----------------------------
# Technology Model
# ----------------------------

class Technology(models.Model):
    """
    Represents a technology with optional parent-child hierarchy.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255, help_text='Technology name')
    description = models.TextField(help_text='Technology description')
    thumbnail_image = models.ImageField(upload_to='technologies/thumbnails/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, help_text='Parent technology')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Technologies'
        ordering = ['title']

    def __str__(self):
        return self.title


# ----------------------------
# Rank Model
# ----------------------------

class Rank(models.Model):
    """
    Represents a rank or position.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, help_text='Rank name')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Ranks'
        ordering = ['name']

    def __str__(self):
        return self.name


# ----------------------------
# Team Model
# ----------------------------

class Team(models.Model):
    """
    Represents a team member with social links.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    position_number = models.PositiveSmallIntegerField(help_text='Position number')
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, help_text='Team member rank')
    profile_image = models.ImageField(upload_to='team/profiles/', blank=True, null=True)
    description = models.TextField(help_text='Team member description')

    facebook_link = models.URLField(blank=True, null=True, help_text='Facebook profile')
    instagram_link = models.URLField(blank=True, null=True, help_text='Instagram profile')
    linkedin_link = models.URLField(blank=True, null=True, help_text='LinkedIn profile')
    twitter_link = models.URLField(blank=True, null=True, help_text='Twitter profile')
    github_link = models.URLField(blank=True, null=True, help_text='GitHub profile')

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# ----------------------------
# Faqs Model
# ----------------------------

class Faq(models.Model):
    """
    Represents a Frequently Asked Question.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    question = models.CharField(max_length=255, help_text='FAQ question')
    answer = models.TextField(help_text='FAQ answer')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
