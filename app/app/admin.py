from django.contrib import admin
from app.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date']


admin.site.register(Video, VideoAdmin)