from django.urls import include, path
from controlpanel import views

from newsletters.views import control_newsletter, control_newsletter_list
from .views import blog_view, blog_detail_view, delete_blog_view
app_name='controlpanel'

#Home page for all 

#for staff blog list and blog detail (staff published and drafted blog post and all published blog post)

#for superuser blog list and blog detail (1.superuser blog post, 2.all published blog post 3.and all awaiting to publish blog post)


#number views for all blog posts
# number of views for home page
#number of views for each course 
#
#  




urlpatterns = [

    path('newsletter',control_newsletter, name='control_newsletter'),
    path('newsletter-list',control_newsletter_list, name='control_newsletter_list '),


    path('control/',blog_view, name='blog_view'),
    path('control/blog/detail/<slug:slug>/<int:pk>/',blog_detail_view, name='blog_detail_view '),
    path('control/delete/<slug:slug>/<int:pk>/',delete_blog_view, name='delete_blog_view '),

]




