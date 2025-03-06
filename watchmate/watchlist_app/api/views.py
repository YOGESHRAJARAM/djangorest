from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializer import MovieSerializer
from rest_framework.views import APIView

class Movie_listAV(APIView):
   
   def get(self,request):
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies,many=True)
            return Response(serializer.data)
   def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class Movle_DetailsAV(APIView):
     
     def get_movie(self,pk):
          try:
             return Movie.objects.get(pk=pk)
          except Movie.DoesNotExist:
              return None
            
          
     def get(self,request,pk):
          movie = self.get_movie(pk)
          serializer = MovieSerializer(movie)
          return Response(serializer.data)
     
     def put(self,request,pk):
            movie = self.get_movie(pk)
            serializer = MovieSerializer(movie,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        
     def delete(self,pk,request):
            movie = self.get_movie(pk)
            movie.delete()
            return Response()
            






# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response()