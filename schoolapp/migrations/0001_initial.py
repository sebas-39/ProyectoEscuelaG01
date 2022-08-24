# Generated by Django 4.1 on 2022-08-10 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_estudiante', models.CharField(max_length=12)),
                ('acudiente', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=14)),
                ('direccion', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.estudiante')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_profesor', models.CharField(max_length=12)),
                ('telefono', models.CharField(max_length=14)),
                ('direccion', models.CharField(blank=True, max_length=50)),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.programa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.profesor'),
        ),
        migrations.AddField(
            model_name='materia',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.programa'),
        ),
    ]
