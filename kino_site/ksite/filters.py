from django_filters import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'status_movie': ['exact'],
            'genre': ['exact'],
            'country': ['exact'],
            'director': ['exact'],
            'actor': ['exact'],
            'year': ['gt', 'lt']

        }


