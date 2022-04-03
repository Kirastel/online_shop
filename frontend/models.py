from django.db import models

class Slider_Content(models.Model):
    header_text = models.CharField(max_length=30)
    text = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='photos/slider/', default='default.jpg')
    url = models.CharField(blank=True, max_length=30)
    text_url = models.CharField(max_length=20)

    def __str__(self):
        return self.header_text

