from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
]
