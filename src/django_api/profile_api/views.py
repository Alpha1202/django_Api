from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API view."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'it is similar to a traditional django view',
            'Gives you the most control over your logic',
            'it is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Respnse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""


        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Updates only the fields required in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method': 'delete'})