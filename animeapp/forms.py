from django.forms import ModelForm
from .animes import Anime
from .models import Document

class AddAnime(ModelForm):
    class Meta:
        model = Anime
        exclude = ()

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('csvFile', )
