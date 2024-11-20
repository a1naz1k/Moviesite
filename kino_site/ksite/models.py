from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from multiselectfield import MultiSelectField


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18),
                                                       MaxValueValidator(110)]
    )
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f' {self.last_name} - {self.first_name}'


class Country (models.Model):
    country_name = models.CharField(max_length=32,)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    director_image = models.ImageField(upload_to='director_images/')

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField
    age = models.PositiveSmallIntegerField
    actor_image = models.ImageField(upload_to='actor_images/')

    def __str__(self):
        return self.actor_name


class Genres(models.Model):
    genres_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.genres_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=32)
    year = models.DateField(auto_now_add=True, blank=True)
    country = models.ForeignKey(Country, related_name='movie_country', on_delete=models.CASCADE)
    director = models.ForeignKey(Director, related_name='movie_director', on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, related_name='movie_actor', on_delete=models.CASCADE)
    TYPES_CHOICES = (
        (144, 144),
        (360, 360),
        (480, 480),
        (720, 720),
        (1080, 1080),
    )
    types = MultiSelectField(choices=TYPES_CHOICES)
    description = models.TextField(blank=True, null=True)
    movie_trailer = models.FileField(upload_to='vid/', verbose_name='Видео', null=True, blank=True)
    movie_image = models.ImageField(upload_to='img/', null=True, blank=True)
    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    )
    status_movie = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')
    genre = models.ManyToManyField(Genres)




    def __str__(self):
        return self.movie_name


    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class MovieLanguages(models.Model):
    language = models.CharField(max_length=64)
    video = models.FileField(upload_to='vid/', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.language


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return f'{self.movie} Moment'


class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="ratings", on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг")
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.movie} - {self.stars}'


class Favorite(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} Favorite'


class FavoriteMovie(models.Model):
    cart = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.favorite} - {self.movie}'


class History(models.Model):
    user = models.ForeignKey(Profile, related_name='history', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='history', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} viewed {self.movie} at {self.viewed_at}'



