from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from root.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT

urlpatterns = []

""" INTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('', include('src.website.urls')),
]

""" EXTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('admin/', admin.site.urls),

]

""" STATIC AND MEDIA FILES ----------------------------------------------------------------------------------------- """
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]
urlpatterns += [
    # Other URL patterns
    path("__reload__/", include("django_browser_reload.urls")),
]