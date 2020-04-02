from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from item.models import *

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['catalog','index','about_us','contacts','reviews']

    def location(self, item):
        return reverse(item)


class CatalogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return Category.objects.all()

class ItemsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return Item.objects.filter(category__isnull=False)
# class BlogSitemap(Sitemap):
#     changefreq = "monthly"
#     priority = 0.5
#     def items(self):
#         return BlogPost.objects.all()
#
#     def lastmod(self, obj):
#         return obj.created_at

