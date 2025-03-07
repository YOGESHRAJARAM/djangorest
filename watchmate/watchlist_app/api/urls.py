from django.urls import path
from watchlist_app.api.views import StreamPlatformAV,WatchListAV,WatchList_DetailsAV,Stream_DetailsAV

urlpatterns = [
    path('list/',WatchListAV.as_view(),name = 'watchlist'),
    path('<int:pk>',WatchList_DetailsAV.as_view(),name = 'watchlist_detail'),
    path('stream/',StreamPlatformAV.as_view(),name = 'stream'),
    path('stream/<int:pk>',Stream_DetailsAV.as_view(),name = 'stream_list'),

]