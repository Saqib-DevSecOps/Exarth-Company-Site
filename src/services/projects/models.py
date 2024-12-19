import uuid

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class ProjectCustomer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='projects/customers/', blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Customer'
        verbose_name_plural = 'Project Customers'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='projects/categories/')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    PROJECT_TIER = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    tag_line = models.CharField(max_length=255, help_text='Enter a tag line for the project')
    logo = models.ImageField(upload_to='projects/logos/', null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='projects/thumbnails/', null=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE,
                                 help_text='Select a category for the project')
    customer = models.ForeignKey(ProjectCustomer, on_delete=models.CASCADE,
                                 help_text='Select a customer for the project')
    start_date = models.DateField(help_text='Enter the project start date', null=True, blank=True)
    end_date = models.DateField(help_text='Enter the project end date', null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.TextField("Short Description", max_length=500, help_text='Enter a short description')
    project_url = models.URLField(null=True, blank=True, help_text='Enter the project URL')
    content = CKEditor5Field('Content', config_name='extends')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    project_technologies = models.ManyToManyField('company.Technology', through='ProjectTechnology')
    project_tier = models.CharField(max_length=20, choices=PROJECT_TIER, default='basic')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_project_testimonial(self):
        try:
            return ProjectTestimonial.objects.get(project=self.id)
        except ProjectTestimonial.DoesNotExist:
            return None


class ProjectKeyFeature(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='key_features')
    position = models.PositiveSmallIntegerField(default=0)
    thumbnail_image = models.ImageField(upload_to='projects/key_features/', null=True, blank=True)
    feature_name = models.CharField(max_length=255, help_text='Feature Name (e.g. Employee Tracking)')
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Key Feature'
        verbose_name_plural = 'Project Key Features'

    def __str__(self):
        return self.feature_name


class ProjectChallenge(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='challenges')
    name = models.CharField(max_length=255, help_text='Enter the project challenge name', verbose_name='Challenge Name',
                            null=True, blank=True)
    challenge = CKEditor5Field('Challenge', config_name='extends', help_text='Enter the project challenge')
    solution = CKEditor5Field('Solution', config_name='extends', help_text='Enter the project solution')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Challenge'
        verbose_name_plural = 'Project Challenges'
        ordering = ['challenge']

    def __str__(self):
        return self.project.title


class ProjectTechnology(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    technology = models.ForeignKey('company.Technology', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Technology'
        verbose_name_plural = 'Project Technologies'
        ordering = ['technology']

    def __str__(self):
        return self.technology.title


class ProjectImage(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/images/', help_text='Upload an image for the project')
    description = models.TextField(blank=True, help_text='Enter a description for the image')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'

    def __str__(self):
        return f"Image for {self.project.title}"


class ProjectVideo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='Select a project for the video')
    video = models.FileField(upload_to='projects/videos/', help_text='Upload a video for the project', null=True,
                             blank=True)
    description = models.TextField(blank=True, help_text='Enter a description for the video', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Video'
        verbose_name_plural = 'Project Videos'

    def __str__(self):
        return f"Video for {self.project.title}"


class ProjectTestimonial(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='testimonial')
    customer = models.ForeignKey(ProjectCustomer, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    testimonial = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Testimonial'
        verbose_name_plural = 'Project Testimonials'

    def __str__(self):
        return f"Testimonial for {self.project.title}"
