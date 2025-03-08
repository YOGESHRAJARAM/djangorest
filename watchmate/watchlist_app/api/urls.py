from django.urls import path
from watchlist_app.api.views import StreamPlatformAV,WatchListAV,WatchList_DetailsAV,Stream_DetailsAV,ReviewDetails,ReviewList

urlpatterns = [
    path('list/',WatchListAV.as_view(),name = 'watchlist'),
    path('<int:pk>',WatchList_DetailsAV.as_view(),name = 'watchlist_detail'),
    path('stream/',StreamPlatformAV.as_view(),name = 'stream'),
    path('stream/<int:pk>',Stream_DetailsAV.as_view(),name = 'stream_list'),
    path('review/',ReviewList.as_view(),name='review'),
    path('review/<int:pk>',ReviewDetails.as_view(),name="review_detail")
]