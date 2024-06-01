from django import forms
from album.models import AlbumModel
rating_choices = [ (i , str(i)) for i in range(1,6)]
class AlbumForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect
    )
    class Meta:
        model = AlbumModel
        fields = '__all__'
        
        widgets = {
            'albumReleaseDate' : (forms.DateInput(attrs={'type' : 'date'})),
            # 'rating' : (forms.ChoiceField(choices=rating_choices))
        }