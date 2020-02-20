from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', admin.site.urls),
    url(r'blog/', include('blog.urls', namespace='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
