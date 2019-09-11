from django.contrib import admin
from .models import Page, Text, Social, Sponsor, News
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('get_display_title', 'slug', 'layout', 'published', 'show_in_menu', 'is_home_page', 'order_buttons')
    exclude = ('order',)
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('order/inc/<int:pk>/', self.inc),
            path('order/dec/<int:pk>/', self.dec),
        ]
        return my_urls + urls
        
    def inc(self, request, pk):
        page = Page.objects.get(pk=pk);
        if page:
            pages = Page.objects.filter(parent=page.parent).order_by('-order');
            prev_page = None;
            for p in pages:
                if p.order > page.order:
                    prev_page = p;
                else:
                    break;
            if prev_page:
                prev_page.order, page.order = page.order, prev_page.order
                page.save(reorder=False);
                prev_page.save();
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def dec(self, request, pk):
        page = Page.objects.get(pk=pk);
        if page:
            pages = Page.objects.filter(parent=page.parent).order_by('order');
            prev_page = None;
            for p in pages:
                if p.order < page.order:
                    prev_page = p;
                else:
                    break;
            if prev_page:
                prev_page.order, page.order = page.order, prev_page.order
                page.save(reorder=False);
                prev_page.save();
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

admin.site.register(Text)
admin.site.register(Social)
admin.site.register(Sponsor)
admin.site.register(News)
