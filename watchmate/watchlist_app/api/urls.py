from django.urls import path
from watchlist_app.api.views import Movie_listAV,Movle_DetailsAV

urlpatterns = [
    path('list/',Movie_listAV.as_view(),name = 'movie_list'),
    path('<int:pk>',Movle_DetailsAV.as_view(),name = 'movie_details')

]