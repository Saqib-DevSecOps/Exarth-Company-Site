from django.urls import path
from .views import (
    HomeView, AboutView, ContactView, ServicesView, ServiceDetailsView, TeamView, BlogView
)
app_name = 'website'
urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServicesView.as_view(), name='services'),
    path('service-details/', ServiceDetailsView.as_view(), name='service-details'),
    path('team/', TeamView.as_view(), name='team'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-details/', BlogView.as_view(), name='blog-details'),

]