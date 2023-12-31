# Generated by Django 4.2.1 on 2023-06-11 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('biografia', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Modifiche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nome')),
                ('email_adress', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Modifiche che vuoi inviarci')),
            ],
        ),
        migrations.CreateModel(
            name='Opera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=250)),
                ('descrizione', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artista', to='mostra.artista')),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Collezione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominativo', models.CharField(max_length=250)),
                ('info', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('proprietario', models.CharField(max_length=250)),
                ('opera', models.ManyToManyField(related_name='opera', to='mostra.opera')),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
    ]
