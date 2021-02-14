
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
# from paystack import urls

# Hello, I am currently experiencing this problem and even the issue i opened about a week ago has not been attended to. Hopefully you have found a work around @inaju

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletters/', include('newsletters.urls', namespace='newsletters')),
    path('controlpanel/', include('controlpanel.urls', namespace='controlpanel')),
    path('course/', include('courses.urls', namespace='courses')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('core.urls', namespace='core')),
    path('', include('users.urls', namespace='users')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

