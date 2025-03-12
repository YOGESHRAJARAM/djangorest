from rest_framework.decorators import api_view
from user_app.api.serializers import Registerserializer
from rest_framework.response import Response
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST',])
def logout_views(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        

@api_view(['POST',])
def registrationview(request):

    if request.method == 'POST':
        serializer = Registerserializer(data=request.data)

        data={}

        if serializer.is_valid():
           
            accounts = serializer.save()
            data['responce'] = "Registeration Successfully"
            data['username'] = accounts.username
            data['email'] = accounts.email

            token = Token.objects.get(user=accounts).key
            data["token"] = token

        else:
            data = serializer.errors

        return Response(data)
