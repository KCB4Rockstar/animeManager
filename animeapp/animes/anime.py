import uuid
from django.db import models
from django.db.models import (
    UUIDField,
    CharField,
    IntegerField,
    FloatField,
    DateTimeField,
    ImageField
)

class Anime(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100, blank=False)
    genre = CharField(max_length=1000, blank=False)
    TV = "TV/Series"
    MOVIE = "Movie"
    SPECIAL = "Special"
    OVA = "OVA"
    UNKNOWN = "Unknown"
    MUSIC = "Music"
    ONA = "ONA"
    typeChoices = (
        (TV, "TV/Series"),
        (MOVIE, "Movie"),
        (SPECIAL, "Special"),
        (OVA, "OVA"),
        (ONA, "ONA"),
        (MUSIC, "Music"),
        (UNKNOWN, "Unknown")
    )
    animeType = CharField(max_length=10, choices=typeChoices, default=TV, blank="False")
    episodes = IntegerField()
    rating = FloatField()
    members = IntegerField()
    created = DateTimeField(auto_now_add=True)
    photoCover = ImageField(null=True, upload_to="img/covers", max_length=1000, verbose_name="cover photo", blank=True)

    class Meta:
        ordering = ("rating",)
