from django.contrib import admin
from .models import ImageUpload

@admin.register(ImageUpload)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image','date']