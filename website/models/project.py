from django.db import models

class Project(models.Model):
    DISPLAY_CHOICES = (
        ('full_image','full_image'),
        ('image_text','image_text')
    )

    name = models.CharField(max_length=100,)
    display = models.CharField(max_length=100,choices=DISPLAY_CHOICES, default='image_text')
    image = models.CharField(max_length=100,)
    image_alt = models.CharField(max_length=100,)
    description = models.CharField(max_length=100,)
    full_text = models.TextField()

