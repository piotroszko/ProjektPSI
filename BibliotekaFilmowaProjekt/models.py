# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Filmy(models.Model):
    id_filmu = models.AutoField(primary_key=True)
    nazwa_filmu = models.TextField()
    opis_filmu = models.TextField(blank=True, null=True)
    id_rezysera = models.ForeignKey('Rezyserowie', models.DO_NOTHING, db_column='id_rezysera')
    id_scenarzysty = models.ForeignKey('Scenarzysci', models.DO_NOTHING, db_column='id_scenarzysty')

    class Meta:
        managed = False
        db_table = 'filmy'
        unique_together = (('id_filmu', 'id_rezysera', 'id_scenarzysty'),)


class Recenzje(models.Model):
    id_recenzji = models.AutoField(primary_key=True)
    tekst = models.TextField(blank=True, null=True)
    ocena = models.IntegerField()
    id_uzytkownika = models.ForeignKey('Uzytkownicy', models.DO_NOTHING, db_column='id_uzytkownika')
    id_filmu = models.ForeignKey(Filmy, models.DO_NOTHING, db_column='id_filmu')

    class Meta:
        managed = False
        db_table = 'recenzje'
        unique_together = (('id_recenzji', 'id_uzytkownika', 'id_filmu'),)


class Rezyserowie(models.Model):
    id_rezysera = models.AutoField(primary_key=True)
    imie = models.TextField()
    nazwisko = models.TextField()

    class Meta:
        managed = False
        db_table = 'rezyserowie'


class Scenarzysci(models.Model):
    id_scenarzysty = models.AutoField(primary_key=True)
    imie = models.TextField()
    nazwisko = models.TextField()

    class Meta:
        managed = False
        db_table = 'scenarzysci'


class Uzytkownicy(models.Model):
    id_uzytkownika = models.AutoField(primary_key=True)
    nazwa = models.TextField(blank=True, null=True)
    haslo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uzytkownicy'
