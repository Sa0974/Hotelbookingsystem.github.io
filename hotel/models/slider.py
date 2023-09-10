from django.db import models

class Slider(models.Model):
    image = models.ImageField(upload_to='uploads/slider')
    caption = models.CharField(max_length=200)

