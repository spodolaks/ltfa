from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fieldsets = [
        (None, {'fields': ('title', 'slug', 'content', 'layout', 'show_in_menu', 'is_home_page')}),
    ]

admin.site.register(Page, PageAdmin)
