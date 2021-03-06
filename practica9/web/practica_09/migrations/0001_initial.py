# Generated by Django 2.2.9 on 2020-01-03 00:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoMusical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_fundacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('estilo_musical', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=100)),
                ('latitud', models.FloatField(blank=True)),
                ('longitud', models.FloatField(blank=True)),
                ('grupos_musicales', models.ManyToManyField(to='practica_09.GrupoMusical')),
                ('instrumento_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='principal', to='practica_09.Instrumentos')),
                ('instrumentos_secundarios', models.ManyToManyField(blank=True, related_name='secundarios', to='practica_09.Instrumentos')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('distribuidora', models.CharField(max_length=200)),
                ('fecha_lanzamiento', models.DateField()),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practica_09.GrupoMusical')),
            ],
        ),
    ]
