from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'phone_number', 'status']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['genres_name']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video', 'movie']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie', 'movie_moments']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'movie', 'stars', 'parent', 'text', 'created_date']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'created_date']


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ['cart', 'movie']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']


class MovieListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'description', 'movie_trailer', 'average_rating', 'movie_image']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class DirectorSerializer(serializers.ModelSerializer):
    movie_director = MovieListSerializer(read_only=True,many=True)
    class Meta:
        model = Director
        fields = ['director_name', 'bio', 'age', 'director_image','movie_director']


class ActorSerializer(serializers.ModelSerializer):
    movie_actor = MovieListSerializer(read_only=True,many=True)
    class Meta:
        model = Actor
        fields = ['director_name', 'bio', 'age', 'director_image']


class MovieDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    country = CountrySerializer()
    ratings = RatingSerializer(many=True, read_only=True)
    director = DirectorSerializer()
    actor = ActorSerializer()
    year = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director', 'actor', 'types',
                  'description', 'movie_trailer', 'movie_image', 'status_movie', 'average_rating', 'genre', 'ratings', ]

    def get_average_rating(self, obj):
        return obj.get_average_rating()
