from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import FilmySerializer
from .models import Filmy

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
#tDo: reszta