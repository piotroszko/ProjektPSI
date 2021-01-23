from rest_framework import serializers
from .models import Filmy,Recenzje,Rezyserowie,Scenarzysci,Uzytkownicy

class FilmySerializer(serializers.HyperlinkedModelSerializer):
    id_filmu = serializers.IntegerField()
    nazwa_filmu = serializers.CharField()
    opis_filmu = serializers.CharField()
    id_rezysera = serializers.SlugRelatedField(queryset=Rezyserowie.objects.all(), slug_field='nazwisko')
    id_scenarzysty = serializers.SlugRelatedField(queryset=Scenarzysci.objects.all(), slug_field='nazwisko')

    class Meta:
        model = Filmy
        fields = ['id_filmu', 'nazwa_filmu', 'opis_filmu', 'id_rezysera', 'id_scenarzysty']

class RecenzjeSerializer(serializers.HyperlinkedModelSerializer):
    id_recenzji = serializers.IntegerField()
    tekst = serializers.CharField()
    ocena = serializers.IntegerField(min_value=0, max_value=10)
    id_uzytkownika = serializers.SlugRelatedField(queryset=Uzytkownicy.objects.all(), slug_field='nazwa')
    id_filmu = serializers.SlugRelatedField(queryset=Rezyserowie.objects.all(), slug_field='nazwa_filmu')
    class Meta:
        model = Recenzje
        fields = ['id_recenzji', 'tekst', 'ocena', 'id_uzytkownika', 'id_filmu']

class RezyserowieSerializer(serializers.HyperlinkedModelSerializer):
    id_rezysera = serializers.IntegerField()
    imie = serializers.CharField()
    nazwisko = serializers.CharField()
    class Meta:
        model = Rezyserowie
        fields = ['id_rezysera', 'imie', 'nazwisko']

class ScenarzysciSerializer(serializers.HyperlinkedModelSerializer):
    id_scenarzysty = serializers.IntegerField()
    imie = serializers.CharField()
    nazwisko = serializers.CharField()
    class Meta:
        model = Scenarzysci
        fields = ['id_scenarzysty', 'imie', 'nazwisko']

class ScenarzysciSerializer(serializers.HyperlinkedModelSerializer):
    id_uzytkownika = serializers.IntegerField()
    nazwa = serializers.CharField()
    haslo = serializers.CharField(max_length=72)
    class Meta:
        model = Filmy
        fields = ['id_zutykownika', 'nazwa', 'haslo']