from django.shortcuts import render,redirect
from album.forms import AlbumForm
from album.models import AlbumModel
from . import models
# Create your views here.
def album(request):
    if(request.method == 'POST'):
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm(request.POST)
    return render(request,'album.html',{'form':form})
def edit_album(request,id):
    album = AlbumModel.objects.get(pk = id)
    album_form = AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        return render(request,'album.html',{'form' : album_form})
def delete_album(request,id):
    album = AlbumModel.objects.get(pk = id)
    album.delete()
    return redirect('homepage')