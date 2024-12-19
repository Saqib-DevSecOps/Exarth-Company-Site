from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from sympy.integrals.meijerint_doc import category

from src.services.projects.models import Project, ProjectCategory
from src.services.resources.models import Blog
from src.services.services.models import Service


# Create your views here.

class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class AboutView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        return context


class ServiceListView(ListView):
    model = Service
    template_name = 'website/service_list.html'


class ServiceDetailView(DetailView):
    template_name = 'website/service_detail.html'
    model = Service

    def get_object(self, queryset=None):
        return get_object_or_404(Service, pk=self.kwargs['pk'])


class ProjectListView(ListView):
    model = Project
    template_name = 'website/project_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        project_category_param = self.request.GET.get('category')
        if category:
            context['project_list'] = Project.objects.filter(category__name=project_category_param)
        else:
            context['project_list'] = Project.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'website/project_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Project, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['similar_project'] = Project.objects.filter(category=self.object.category)
        return context


class ContactView(TemplateView):
    template_name = 'website/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context


class TeamView(TemplateView):
    template_name = 'website/team_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Team'
        return context


class BlogListView(ListView):
    model = Blog
    template_name = 'website/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class BlogDetailView(DetailView):
    template_name = 'website/blog_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Blog, pk=self.kwargs['pk'])
