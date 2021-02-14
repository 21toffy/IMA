from django.shortcuts import render
from blog.models import *
from courses.models import *
from users.models import *
from django.shortcuts import render, get_object_or_404,redirect

from django.contrib.auth.decorators import login_required
from .forms import *
import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from core.models import ViewCount

def blog_view(request):

    if request.user.is_staff:#to check if the user is eligible to view this page
        
        pub_blog = Blog.objects.filter(category="Blog Post", status=1)
        event_blog = Blog.objects.filter(category="Event", status=1)
        my_Posts = Blog.objects.filter(author = request.user)
        awaiting_approval = Blog.objects.filter(author = request.user, status=0)
        my_blog = Blog.objects.filter(author=request.user) #getting the list of request.users blog posts

        #all blog posts awating approval, this view is is only seen by a super user
        super_approval = Blog.objects.filter(status=0)


        #counting pages views
        home_count = ViewCount.objects.filter(page='Home')
        about_count = ViewCount.objects.filter(page='About')
        courses_count = ViewCount.objects.filter(page='Courses')
        blog_count = ViewCount.objects.filter(page='Blog')
        contact_count = ViewCount.objects.filter(page='Contact')


        #this logic is to count the total number of blog views i.e Sums up all the views of all the blogs in the DB
        a = Blog.objects.all()
        x = []
        for i in a:
            x.append(i.view)
        all_views=sum(x)

        #this logic is to count the total number of blog views of a particular user (request.user) i.e Sums up all the views of all the blogs associated with a user in the DB
        b= Blog.objects.filter(author=request.user)
        y = []
        for i in b:
            y.append(i.view)
        my_views = sum(y)

        #form for creating a blog post   
        if request.method == 'POST':
            form = Blog_form(request.POST)
            if form.is_valid():
                new_blog = form.save(commit=False)
                new_blog.author = request.user
                new_blog.save()
                messages.success(request, '{} added awaiting corrections and Approval'.format(new_blog.title), "alert alert-error alert-dismissible")
                return HttpResponseRedirect(reverse('controlpanel:blog_view'))
            # else:
            #     messages.error(request, new_blog.errors , "alert alert-error alert-dismissible")
            #     return HttpResponseRedirect(reverse('controlpanel:blog_view'))

        else:
            form=Blog_form()
    else:
        return HttpResponseRedirect(reverse('core:home'))
    context = {'user':request.user, 'my_blog':my_blog, 'form':form, 'pub_blog':pub_blog, 'event_blog':event_blog, 'my_Posts':my_Posts, 'awaiting_approval':awaiting_approval, 'super_approval':super_approval, 'all_views':all_views, 'my_views':my_views,    'home_count':home_count,
    'about_count':about_count,
    'courses_count':courses_count,
    'blog_count':blog_count,
    'contact_count':contact_count,
    
    }
    return render(request,'controlpanel/blog_list_blog_create.html',context)

        

def blog_detail_view(request,slug=None,pk= None):
    if request.user.is_staff:
        my_blog = get_object_or_404(Blog, pk=pk, slug=slug)

        if request.user == my_blog.author:
            if request.method=="POST":
                form =Edit_Blog_form(request.POST, instance=my_blog)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'blog edited succesfully', "alert alert-success alert-dismissible")
                else:
                    messages.error(request, form.errors , "alert alert-error alert-dismissible")
                    return HttpResponseRedirect(reverse('controlpanel:blog_detail'))

            else:
                form =Edit_Blog_form(instance=my_blog)
    else:
        return HttpResponseRedirect(reverse('core:home'))
    context = {'user':request.user, 'my_blog':my_blog, 'form':form}
    return render(request,'controlpanel/blog_detail.html')
    


def delete_blog_view(request, slug, pk):
    if request.user.is_staff:
        my_blog = get_object_or_404(Blog, pk=pk, slug=slug)
        if request.user == my_blog.author:
            if request.method=='POST':
                blog.delete()
                messages.success(request, 'blog has been deleted', extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('controlpanel:blog_view')
        else:
            messages.error(request, 'blog can not be deleted by you stop trying stupid things you will be blocked', extra_tags='alert alert-error alert-dismissible fade show')

    else:
        messages.error(request, 'blog can not be deleted by you stop trying stupid things you will be blocked', extra_tags='alert alert-error alert-dismissible fade show')
        return redirect(reverse('controlpanel:blog_view'))

    # context = {'user':request.user, 'my_blog':my_blog, 'form':form}
    return render(request,'controlpanel/blog_confirm_delete.html')

