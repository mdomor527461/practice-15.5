from django.shortcuts import render
from album.models import AlbumModel

def home(request):
    data = AlbumModel.objects.all()
    return render(request,'base.html',{'data' : data})

        