from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import FilmySerializer, RecenzjeSerializer, RezyserowieSerializer, ScenarzysciSerializer
from .models import Filmy,Recenzje,Rezyserowie,Scenarzysci

class ListaFilmow(generics.ListCreateAPIView):
    def get(self, request, format=None):
        queryset = Filmy.objects.all()
        serializer = FilmySerializer(queryset)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = FilmySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Recenzje(generics.ListCreateAPIView):
    def get(self, request, format=None):
        queryset = Recenzje.objects.all()
        serializer = RecenzjeSerializer(queryset)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = RecenzjeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Rezyserowie(generics.ListCreateAPIView):
    def get(self, request, format=None):
        queryset = Rezyserowie.objects.all()
        serializer = RezyserowieSerializer(queryset)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = RezyserowieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Scenarzysci(generics.ListCreateAPIView):
    def get(self, request, format=None):
        queryset = Scenarzysci.objects.all()
        serializer = ScenarzysciSerializer(queryset)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ScenarzysciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)