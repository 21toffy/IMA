from django.urls import include, path
from . import views


app_name='blog'

# 
urlpatterns = [

    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('events/', views.EventListView.as_view(), name='event_post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]



