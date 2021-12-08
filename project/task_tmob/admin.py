from django.contrib import admin
from .models import Redirect
from django.contrib.auth.models import Group

class RedirectConfigAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "updated_at", "created_at",]
    ordering = ("-id", "updated_at",)
    list_display = ("id", "key", "created_at", 'updated_at',)
    list_filter = ('key', 'url',)
    search_fields = ("key", "url",)

admin.site.register(Redirect, RedirectConfigAdmin)
admin.site.unregister(Group)
