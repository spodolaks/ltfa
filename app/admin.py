from django.contrib import admin
from .models import Page, Text, Social, Sponsor, News

class PageAdmin(admin.ModelAdmin):
    list_display = ('get_display_title', 'slug', 'published', 'order', 'sort')
    exclude = ('sort',)

admin.site.register(Page, PageAdmin)
admin.site.register(Text)
admin.site.register(Social)
admin.site.register(Sponsor)
admin.site.register(News)
