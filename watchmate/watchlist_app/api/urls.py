from django.urls import path,include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import ReviewCreat,StreamPlatformVS,WatchListAV,WatchList_DetailsAV,ReviewDetails,ReviewList

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='Streamplatform')

urlpatterns = [
    path('list/',WatchListAV.as_view(),name = 'watchlist'),
    path('<int:pk>',WatchList_DetailsAV.as_view(),name = 'watchlist_detail'),
    # path('stream/',StreamPlatformAV.as_view(),name = 'stream'),
    # path('stream/<int:pk>',Stream_DetailsAV.as_view(),name = 'stream_list'),
    path('',include(router.urls)),
    path('stream/<int:pk>/review-create',ReviewCreat.as_view(),name='review_create'),
    path('stream/<int:pk>/review',ReviewList.as_view(),name='review_list'),
    path('stream/review/<int:pk>',ReviewDetails.as_view(),name="review_detail")
]