from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.sitemaps.views import sitemap
#from sitemaps import StaticViewSitemap
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('financas/', include('financas.urls', namespace='financas' )), 
    path('admin/', admin.site.urls),
]
