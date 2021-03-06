# Generated by Django 3.1 on 2021-01-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmy',
            fields=[
                ('id_filmu', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa_filmu', models.TextField()),
                ('opis_filmu', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'filmy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recenzje',
            fields=[
                ('id_recenzji', models.AutoField(primary_key=True, serialize=False)),
                ('tekst', models.TextField(blank=True, null=True)),
                ('ocena', models.IntegerField()),
            ],
            options={
                'db_table': 'recenzje',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rezyserowie',
            fields=[
                ('id_rezysera', models.AutoField(primary_key=True, serialize=False)),
                ('imie', models.TextField()),
                ('nazwisko', models.TextField()),
            ],
            options={
                'db_table': 'rezyserowie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scenarzysci',
            fields=[
                ('id_scenarzysty', models.AutoField(primary_key=True, serialize=False)),
                ('imie', models.TextField()),
                ('nazwisko', models.TextField()),
            ],
            options={
                'db_table': 'scenarzysci',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uzytkownicy',
            fields=[
                ('id_uzytkownika', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.TextField(blank=True, null=True)),
                ('haslo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'uzytkownicy',
                'managed': False,
            },
        ),
    ]
