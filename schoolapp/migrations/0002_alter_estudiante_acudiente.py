# Generated by Django 4.1 on 2022-08-24 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='acudiente',
            field=models.CharField(max_length=180),
        ),
    ]