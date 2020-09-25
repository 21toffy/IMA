from django.urls import include, path
from . import views


app_name='core'

# 
urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
]
