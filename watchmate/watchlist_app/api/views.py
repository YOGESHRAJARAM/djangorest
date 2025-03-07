from rest_framework.response import Response
from watchlist_app.models import StreamPlatform,WatchList
from watchlist_app.api.serializer import WatchListSerializer,StreamPlatformSerializer
from rest_framework.views import APIView

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
            

class StreamPlatformAV(APIView):
   
   def get(self,request):
            movies = StreamPlatform.objects.all()
            serializer = StreamPlatformSerializer(movies,many=True)
            return Response(serializer.data)
   def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Stream_DetailsAV(APIView):
     
     def get_movie(self,pk):
          try:
             return StreamPlatform.objects.get(pk=pk)
          except StreamPlatform.DoesNotExist:
              return None
            
          
     def get(self,request,pk):
          movie = self.get_movie(pk)
          serializer = StreamPlatformSerializer(movie)
          return Response(serializer.data)
     
     def put(self,request,pk):
            movie = self.get_movie(pk)
            serializer = StreamPlatformSerializer(movie,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        
     def delete(self,pk,request):
            movie = self.get_movie(pk)
            movie.delete()
            return Response()
        

