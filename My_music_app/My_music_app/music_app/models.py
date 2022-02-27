from django.core.validators import  MinLengthValidator
from django.db import models

from My_music_app.music_app.validators import only_letters_numbers_and_underscores_validator


class Profile(models.Model):
    USERNAME_MIN_LEN=2
    USERNAME_MAX_LEN=15
    username=models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            only_letters_numbers_and_underscores_validator,
        )
    )
    email=models.EmailField()
    age=models.PositiveIntegerField(
        blank=True,
        null = True,
    )
class Album(models.Model):
    ALBUM_NAME_MAX_LEN=30
    ARTIST_NAME_MAX_LEN = 30
    POP_MUSIC='Pop Music'
    JAZZ_MUSIC='Jazz Music'
    RNB_MUSIC='R&B Music'
    ROCK_MUSIC='Rock Music'
    COUNTRY_MUSIC='Country Music'
    DANCE_MUSIC='Dance Music'
    HIP_HOP_MUSIC='Hip Hop Music'
    OTHER='Other'
    GENRES=[(x,x) for x in (POP_MUSIC,JAZZ_MUSIC,RNB_MUSIC,ROCK_MUSIC,COUNTRY_MUSIC,DANCE_MUSIC,HIP_HOP_MUSIC,OTHER)]


    album_name=models.CharField(
        unique=True,
        max_length=ALBUM_NAME_MAX_LEN
    )
    artist = models.CharField(

        max_length=ARTIST_NAME_MAX_LEN
    )
    genre=models.CharField(
        max_length=max(len(x) for (x, _) in GENRES),
        choices=GENRES
    )
    description=models.TextField(
        null=True,
        blank=True,
    )
    image_url=models.URLField()
    price=models.FloatField(

    )
