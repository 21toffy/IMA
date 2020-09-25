
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path("paystack", include(('paystack.urls','paystack'),namespace='paystack')),
    path('admin/', admin.site.urls),
    path('newsletters/', include('newsletters.urls', namespace='newsletters')),
    path('controlpanel/', include('controlpanel.urls', namespace='controlpanel')),
    path('course/', include('courses.urls', namespace='courses')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('core.urls', namespace='core')),
    path("paystack", include(('paystack.urls','paystack'),namespace='paystack')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

