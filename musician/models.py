from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    instrumentType = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.firstName