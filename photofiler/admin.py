
from django.contrib import admin
from models import Photo

class PhotoAdmin(admin.ModelAdmin):
    class Media:
        js = ['/site_media/js/admin/tiny_django_browser.js', ]
    list_display = ['get_thumbnail_html', 'title']
    list_display_links = ['get_thumbnail_html']
    
admin.site.register(Photo, PhotoAdmin)
