from rest_framework.response import Response
from watchlist_app.models import StreamPlatform,WatchList,Review
from watchlist_app.api.serializer import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class ReviewCreat(generics.CreateAPIView):
    #   queryset = Review.objects.all()
      serializer_class = ReviewSerializer
      def perform_create(self, serializer):
           pk = self.kwargs.get('pk')
           movie = WatchList.objects.get(pk=pk)
           serializer.save(watchlist = movie)

class ReviewList(generics.ListAPIView):
    #   queryset = Review.objects.all()
      serializer_class = ReviewSerializer

      def get_queryset(self):
           pk = self.kwargs.get('pk')
           return Review.objects.filter(watchlist=pk)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
        queryset = Review.objects.all()
        serializer_class = ReviewSerializer

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
     
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewDetails(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#           queryset = Review.objects.all()
#           serializer_class = ReviewSerializer

#           def get(self, request, *args, **kwargs):
#            return self.retrieve(request, *args, **kwargs)

#           def put(self, request, *args, **kwargs):
#              return self.update(request, *args, **kwargs)

#           def delete(self, request, *args, **kwargs):
#              return self.destroy(request, *args, **kwargs)

class WatchListAV(APIView):
   
   def get(self,request):
            movies = WatchList.objects.all()
            serializer = WatchListSerializer(movies,many=True)
            return Response(serializer.data)
   def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        



class WatchList_DetailsAV(APIView):
     
     def get_movie(self,pk):
          try:
             return WatchList.objects.get(pk=pk)
          except WatchList.DoesNotExist:
              return None
            
          
     def get(self,request,pk):
          movie = self.get_movie(pk)
          serializer = WatchListSerializer(movie)
          return Response(serializer.data)
     
     def put(self,request,pk):
            movie = self.get_movie(pk)
            serializer = WatchListSerializer(movie,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        
     def delete(self,pk,request):
            movie = self.get_movie(pk)
            movie.delete()
            return Response()
            

class StreamPlatformVS(viewsets.ViewSet):
 
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)            

# class StreamPlatformAV(APIView):
   
#    def get(self,request):
#             movies = StreamPlatform.objects.all()
#             serializer = StreamPlatformSerializer(movies,many=True)
#             return Response(serializer.data)
#    def post(self,request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class Stream_DetailsAV(APIView):
     
#      def get_movie(self,pk):
#           try:
#              return StreamPlatform.objects.get(pk=pk)
#           except StreamPlatform.DoesNotExist:
#               return None
            
          
#      def get(self,request,pk):
#           movie = self.get_movie(pk)
#           serializer = StreamPlatformSerializer(movie)
#           return Response(serializer.data)
     
#      def put(self,request,pk):
#             movie = self.get_movie(pk)
#             serializer = StreamPlatformSerializer(movie,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
        
#      def delete(self,pk,request):
#             movie = self.get_movie(pk)
#             movie.delete()
#             return Response()
        

