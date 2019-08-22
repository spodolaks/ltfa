from django.contrib import admin
from .models import Page, Text, Social, Sponsor

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fieldsets = [
        (None, {'fields': ('title', 'slug', 'content', 'layout', 'show_in_menu', 'is_home_page')}),
    ]

admin.site.register(Page, PageAdmin)
admin.site.register(Text)
admin.site.register(Social)
admin.site.register(Sponsor)
