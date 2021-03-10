from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='myImage')
    date = models.DateTimeField(auto_now_add=True)