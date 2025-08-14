from django.db import models

# Create your models here.

class File(models.Model):

    filename = models.CharField(max_length=200, null=True, blank=True)   
    
    image = models.ImageField(upload_to="", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    pimage = models.ImageField(upload_to="", null=True, blank=True)
    himage = models.ImageField(upload_to="", null=True, blank=True)
    def __str__(self):
        return self.filename