from django.contrib import admin

from .models import HomeView
from .models import ViewCount

admin.site.register(HomeView)
admin.site.register(ViewCount)