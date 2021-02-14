from django.shortcuts import render, get_object_or_404, HttpResponse
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

from blog.models import Blog
from .models import ViewCount
#first_about:
# 4 images
# https://i.ibb.co/rQRJYpS/Screenshot-317.png
# https://i.ibb.co/rsF4LqS/Screenshot-318.png
# https://i.ibb.co/5GW8wCX/Screenshot-315.png
# https://i.ibb.co/fXqbm3m/Screenshot-316.png 
# to this https://i.ibb.co/pK86NCf/about1.png

#about 600X500 px

#second_about:
# 4 passports 
# about 500x500px

#preloader: 130X25


#logo/preloader
#hero2 background image should be sorted
# first about picture, 
# mission and vission , 
# 2 key deliverables aside skills development, awareness events
# what to fit into testimonials second 6 coloumn
#footer needs a lot of 
#workon contact form
# work on email subscrition form
# ----completed-------- 
#remove blog post from homepage

def home(request):
    homeview = ViewCount.objects.create(page='Home')
    homeview.save()
    print('if blog')
    if Blog:
        blogs=Blog.objects.filter(status=0).order_by('-time')[:3]
    
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        print('form valid')
        email = request.POST.get('email')

        newsletter = NewsletterUser(email=email)

        # newsletter.save()
        # instance = form.save(commit=False)
        print('commit is false')
        if NewsletterUser.objects.filter(email=email).exists():
            messages.warning(request, 'your are already receiving Newsletters from us', "alert alert-warning alert-dismissible")

            print('sorry this email already exists')
        else:
            print('about to be saved cause does not exist')
            newsletter.save()
            messages.success(request, 'your email has been submitted check your inbox', "alert alert-success alert-dismissible")

            subject = "thank you for Joining our NewsLetters"
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            # subscription_message = "welcome to Influenz media... if you will like to unsunscribe visit 127  .0.0.1:8000/newsletter/unsubscribe"
            # send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=subscription_message, fail_silently=False)

            with open(settings.BASE_DIR + "/templates/newsletters/sign_up_email.txt") as f:
                subscription_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=subscription_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/sign_up_email.html").render()
            message.attach_alternative(html_template, "text/html ")
            message.send()
    else:
        print('form not ')
    # context = {}
    # template = 'index.html'
    # return render(request, template, context)

    context={

        'blogs':blogs,
        'form':form

    }

    return render(request, 'index.html', context)



# class AboutView(TemplateView):
#     homeview = ViewCount.objects.create(page='About')
#     homeview.save()
    template_name = 'about.html'


def about(request):
    homeview = ViewCount.objects.create(page='About')
    homeview.save()
    return render(request, 'about.html')



def contact(request):
    homeview = ViewCount.objects.create(page='Contact')
    homeview.save()
    return render(request, 'contact.html')


