from django.db import models
from musician.models import MusicianModel
# Create your models here.
class AlbumModel(models.Model):
    albumName = models.CharField(max_length=255)
    albumReleaseDate = models.DateField()
    rating = models.CharField(max_length=255)
    
    musician = models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.albumName