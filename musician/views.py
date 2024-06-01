from django.shortcuts import render,redirect
from musician.forms import MusicianForm
from musician.models import MusicianModel
# Create your views here.
def musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm(request.POST)
    return render(request,'musician.html',{'form':form})
def edit_musician(request,id):
    musician = MusicianModel.objects.get(pk = id)
    musician_form = MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = MusicianForm(request.Post, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    
    return render(request,'musician.html',{'form' : musician_form})
        
