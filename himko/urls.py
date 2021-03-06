from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from page.sitemaps import *
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static

sitemaps = {
    'static': StaticViewSitemap,
    'category': CatalogSitemap,
    'item': ItemsSitemap

}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    # path('item/', include('item.urls')),
    path('cart/', include('cart.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    # path('user/', include('customuser.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

