from django.shortcuts import render
from django.views.generic import TemplateView


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


class ContactView(TemplateView):
    template_name = 'website/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context


class ServicesView(TemplateView):
    template_name = 'website/service_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Services'
        return context


class ServiceDetailsView(TemplateView):
    template_name = 'website/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Service Details'
        return context


class ProjectListView(TemplateView):
    template_name = 'website/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projects'
        return context


class ProjectDetailsView(TemplateView):
    template_name = 'website/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Project Details'
        return context


class TeamView(TemplateView):
    template_name = 'website/team_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Team'
        return context


class BlogView(TemplateView):
    template_name = 'website/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class BlogDetailsView(TemplateView):
    template_name = 'website/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog Details'
        return context
