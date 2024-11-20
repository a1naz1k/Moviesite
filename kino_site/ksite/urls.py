from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', MovieListViewSet.as_view({'get': 'list', }), name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve',}),
         name='movie_detail'),

    path('profile/', ProfileViewSet.as_view({'get': 'list', }), name='profile_list'),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve',}),
         name='profile_detail'),

    path('country/', CountryViewSet.as_view({'get': 'list', }), name='country_list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve',}),
         name='country_detail'),

    path('director/', DirectorViewSet.as_view({'get': 'list', }), name='director_list'),
    path('director/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', }),
         name='director_detail'),

    path('actor/', ActorViewSet.as_view({'get': 'list', }), name='actor_list'),
    path('actor/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', }),
         name='actor_detail'),

    path('genres/', GenresViewSet.as_view({'get': 'list', }), name='genre_list'),
    path('genres/<int:pk>/', GenresViewSet.as_view({'get': 'retrieve', }),
         name='genre_detail'),

    path('movie_language/', MovieLanguagesViewSet.as_view({'get': 'list', }),
         name='movie_languages_list'),
    path('movie_language/<int:pk>/',
         MovieLanguagesViewSet.as_view({'get': 'retrieve', }),
         name='movie_languages_detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create', }), name='moment_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'put': 'update',
                                                       'delete': 'destroy', 'get': 'retrieve', }),
         name='moment_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', }), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', }),
         name='rating_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create', }), name='favorite_list'),


    path('favorite_movie/', FavoriteMovieViewSet.as_view({'get': 'list', }),
         name='favorite_movie_list'),

    path('history/', HistoryViewSet.as_view({'get': 'list', }), name='history_list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', }),
         name='history_detail'),
]
