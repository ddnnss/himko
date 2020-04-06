from django.contrib import admin
from .models import *
# Register your models here.
class ItemAdmin(admin.ModelAdmin):


    search_fields = ('name',)


    class Meta:
        model = Item
admin.site.register(Category)
admin.site.register(Item,ItemAdmin)