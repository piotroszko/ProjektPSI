from rest_framework import serializers

class FilmySerializer(serializers.Serializer):
    id_filmu = serializers.IntegerField()
    nazwa_filmu = serializers.CharField()
    opis_filmu = serializers.CharField()
    id_rezysera = serializers.IntegerField()
    id_scenarzysty = serializers.IntegerField()

class RecenzjeSerializer(serializers.Serializer):
    id_recenzji = serializers.IntegerField()
    tekst = serializers.CharField()
    ocena = serializers.IntegerField(min_value=0, max_value=10)
    id_uzytkownika = serializers.IntegerField()
    id_filmu = serializers.IntegerField()

class RezyserowieSerializer(serializers.Serializer):
    id_rezysera = serializers.IntegerField()
    imie = serializers.CharField()
    nazwisko = serializers.CharField()

class ScenarzysciSerializer(serializers.Serializer):
    id_scenarzysty = serializers.IntegerField()
    imie = serializers.CharField()
    nazwisko = serializers.CharField()

class ScenarzysciSerializer(serializers.Serializer):
    id_uzytkownika = serializers.IntegerField()
    nazwa = serializers.CharField()
    haslo = serializers.CharField(max_length=72)
