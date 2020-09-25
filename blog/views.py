from django.shortcuts import render, get_object_or_404, HttpResponse
from . models import Blog
from django.utils import timezone
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

from newsletters.forms import NewsletterUserSignUpForm
from newsletters.models import NewsletterUser

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages

from django.template.loader import get_template


class PostListView(ListView):
    model = Blog
    context_object_name='posts'

    ''' Returns  the list of views for this View'''
    def get_queryset(self):
        return Blog.objects.filter(category = "Blog Post").order_by('-time')  #__lte is less than equals too!



class EventListView(ListView):
    model = Blog
    context_object_name='posts'

    ''' Returns  the list of views for this View'''
    def get_queryset(self):
        return Blog.objects.filter(category="Event").order_by('-time')  #__lte is less than equals too!

    

class PostDetailView(DetailView):
    model = Blog
    context_object_name='post_detail'
    
    # def get_context_data(self, **kwargs):
    #     context = super(RoomView, self).get_context_data(**kwargs)
    #     context['workers'] = Worker.objects.all()
    #     print context
    #     return context

    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['blog_list'] = Blog.objects.filter(time__lte=timezone.now()).order_by('-time')[0:10]
        return context
    

