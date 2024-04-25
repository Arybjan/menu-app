from django.contrib import admin
from .models import Menu


class MenuApp(admin.ModelAdmin):
    list_display = ["id", "title", "text"]


admin.site.register(Menu, MenuApp)
