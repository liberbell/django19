from django.db import models

# Create your models here.
class Job(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField()
