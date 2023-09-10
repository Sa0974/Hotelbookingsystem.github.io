from django.db import models


class FrontendSlider(models.Model):
    image = models.ImageField(upload_to='uploads/slider_images/')
    caption = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.caption
