# Django
from django.shortcuts import render
from django.contrib.auth.models import User

# REST Framework
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

# Provider OAuth2
# from provider.oauth2.models import Client


from django.contrib.auth.models import User
from oauth.serializers import ProfileSerializer


class RegistrationView(APIView):
    """ Allow registration of new users. """
    permission_classes = ()

    def post(self, request):
        serializer = ProfileSerializer(data=request.DATA)

        # Check format and unique constraint
        if not serializer.is_valid():
            return Response(serializer.errors,\
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        u = User.objects.create(username=data['username'])
        u.set_password(data['password'])
        u.save()

        # Create OAuth2 client
        # name = u.username
        # client = Client(user=u, name=name, url='' + name,\
        #         client_id=name, client_secret='', client_type=1)
        # client.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)