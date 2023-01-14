from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=7000)
    image = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_2 = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_3 = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_4 = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_5 = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_6 = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_7 = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_8 = models.ImageField(upload_to='portfolio/images/',blank=True)
    image_9 = models.ImageField(upload_to='portfolio/images/',blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
