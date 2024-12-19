from django.urls import path
from .views import (
    HomeView, AboutView, ContactView, ServiceListView, ServiceDetailView, TeamView, BlogListView, ProjectListView,
    ProjectDetailView, BlogDetailView
)

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('service/<str:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('project-list/', ProjectListView.as_view(), name='project-list'),
    path('project/<str:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('team/', TeamView.as_view(), name='team'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<str:pk>/', BlogDetailView.as_view(), name='blog-detail'),

]
