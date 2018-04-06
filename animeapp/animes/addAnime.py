from django.forms import ModelForm
from .anime import Anime

class AddAnime(ModelForm):
    class Meta:
        model = Anime
        exclude = ()